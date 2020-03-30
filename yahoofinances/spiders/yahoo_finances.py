# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class YahooFinancesSpider(scrapy.Spider):
    name = 'yahoo_finances'
    # allowed_domains = ['finance.yahoo.com/quote']

    start_urls = ['https://finance.yahoo.com/quote/AAL?p=AAL','https://finance.yahoo.com/quote/AAPL/?p=AAPL', 'https://finance.yahoo.com/quote/ADBE/?p=ADBE']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(1))

            text = assert(splash:select(".B(8px) Pos(a) C(white) Py(2px) Px(0) Ta(c) Bdrs(3px) Trstf(eio) Trsde(0.5) Arrow South Bdtc(i)::a Fw(b) Bgc($buy) Bdtc($buy)"))
            text = text:text()
            return text
        end
    '''

    # def start_requests(self): 
    #     yield SplashRequest(url="https://finance.yahoo.com/quote/AAL?p=AAL", callback=self.parse, endpoint="execute", args={
    #         'lua_source': self.script
    #     })

    # def start_requests(self):
    #     yield scrapy.Request(url=['https://finance.yahoo.com/quote/AAL?p=AAL', 'https://finance.yahoo.com/quote/JBLU?p=JBLU'], headers={
    #         'User-Agent': self.user_agent
    #     })

    # def set_user_agent(self, request):
    #     request.headers['User-Agent'] = self.user_agent
    #     return request

    def parse(self, response):
        print('response_url', response.url)

        last_chars = response.url.split('/')[4].split('?')[0]
        print('response_url', response.url)
        print('last_chars', last_chars)

        object = {}
        object['stock_symbol'] = last_chars
        for quote in response.xpath("//div[@id='quote-summary']/div[1]/table/tbody/tr"):
            
            print('quote', quote)
            name = quote.xpath(".//td[1]/span/text()").get()
            if name == 'Avg. Volume':
                name = 'Avg Volume'
            value = quote.xpath(".//td[2]/span/text()").get()

            object[name] = value

        for quote in response.xpath("//div[@id='quote-summary']/div[2]/table/tbody/tr"):
            
            print('quote', quote)
            name = quote.xpath(".//td[1]/span/text()").get()
            value = quote.xpath(".//td[2]/span/text()").get()

            object[name] = value

        object['Fair Value'] = response.xpath("//div[@class='IbBox Ta(start) C($tertiaryColor)']/text()").get()
        object['Recommendation Rating'] = response.xpath("//*[@id='Col2-7-QuoteModule-Proxy']/div/section/a/h2/span/text()").get()

        yield object

        # statistics_page = response.xpath("//*[@id='quote-nav']/ul/li[5]/a/@href").get()

        # if statistics_page: 
        yield scrapy.Request(url='https://finance.yahoo.com/quote/{0}/key-statistics?p={0}'.format(last_chars), callback=self.parse_statistics)

    
    def parse_statistics(self, response): 

            object = {}
            
            last_chars = response.url.split('/')[4]
            print('response_url', response.url)
            print('last_chars', last_chars)

            object['stock_symbol'] = last_chars

            # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody

            # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[1]/td[2]

            # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[1]/td[3]

            # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]

            for valuation in response.xpath("//*[@id='Col1-0-KeyStatistics-Proxy']/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody"):    
                print('valuation', valuation)

                object['Market Cap (intraday)_current'] = valuation.xpath(".//tr[1]/td[2]/text()").get()
                object['Market Cap (intraday)_12/31/2019'] = valuation.xpath(".//tr[1]/td[3]/text()").get()
                object['Market Cap (intraday)_9/30/2019'] = valuation.xpath(".//tr[1]/td[4]/text()").get()
                object['Market Cap (intraday)_6/30/2019'] = valuation.xpath(".//tr[1]/td[5]/text()").get()
                object['Market Cap (intraday)_3/31/2019'] = valuation.xpath(".//tr[1]/td[6]/text()").get()
                object['Market Cap (intraday)_12/31/2018'] = valuation.xpath(".//tr[1]/td[7]/text()").get()

                object['Enterprise Value_current'] = valuation.xpath(".//tr[2]/td[2]/text()").get()
                object['Enterprise Value_12/31/2019'] = valuation.xpath(".//tr[2]/td[3]/text()").get()
                object['Enterprise Value_9/30/2019'] = valuation.xpath(".//tr[2]/td[4]/text()").get()
                object['Enterprise Value_6/30/2019'] = valuation.xpath(".//tr[2]/td[5]/text()").get()
                object['Enterprise Value_3/31/2019'] = valuation.xpath(".//tr[2]/td[6]/text()").get()
                object['Enterprise Value_12/31/2018'] = valuation.xpath(".//tr[2]/td[7]/text()").get()

                object['Trailing P/E_current'] = valuation.xpath(".//tr[3]/td[2]/text()").get()
                object['Trailing P/E_12/31/2019'] = valuation.xpath(".//tr[3]/td[3]/text()").get()
                object['Trailing P/E_9/30/2019'] = valuation.xpath(".//tr[3]/td[4]/text()").get()
                object['Trailing P/E_6/30/2019'] = valuation.xpath(".//tr[3]/td[5]/text()").get()
                object['Trailing P/E_3/31/2019'] = valuation.xpath(".//tr[3]/td[6]/text()").get()
                object['Trailing P/E_12/31/2018'] = valuation.xpath(".//tr[3]/td[7]/text()").get()

                object['Forward P/E_current'] = valuation.xpath(".//tr[4]/td[2]/text()").get()
                object['Forward P/E_12/31/2019'] = valuation.xpath(".//tr[4]/td[3]/text()").get()
                object['Forward P/E_9/30/2019'] = valuation.xpath(".//tr[4]/td[4]/text()").get()
                object['Forward P/E_6/30/2019'] = valuation.xpath(".//tr[4]/td[5]/text()").get()
                object['Forward P/E_3/31/2019'] = valuation.xpath(".//tr[4]/td[6]/text()").get()
                object['Forward P/E_12/31/2018'] = valuation.xpath(".//tr[4]/td[7]/text()").get()

                object['PEG Ratio (5 yr expected)_current'] = valuation.xpath(".//tr[5]/td[2]/text()").get()
                object['PEG Ratio (5 yr expected)_12/31/2019'] = valuation.xpath(".//tr[5]/td[3]/text()").get()
                object['PEG Ratio (5 yr expected)_9/30/2019'] = valuation.xpath(".//tr[5]/td[4]/text()").get()
                object['PEG Ratio (5 yr expected)_6/30/2019'] = valuation.xpath(".//tr[5]/td[5]/text()").get()
                object['PEG Ratio (5 yr expected)_3/31/2019'] = valuation.xpath(".//tr[5]/td[6]/text()").get()
                object['PEG Ratio (5 yr expected)_12/31/2018'] = valuation.xpath(".//tr[5]/td[7]/text()").get()

                object['Price/Sales (ttm)_current'] = valuation.xpath(".//tr[6]/td[2]/text()").get()
                object['Price/Sales (ttm)_12/31/2019'] = valuation.xpath(".//tr[6]/td[3]/text()").get()
                object['Price/Sales (ttm)_9/30/2019'] = valuation.xpath(".//tr[6]/td[4]/text()").get()
                object['Price/Sales (ttm)_6/30/2019'] = valuation.xpath(".//tr[6]/td[5]/text()").get()
                object['Price/Sales (ttm)_3/31/2019'] = valuation.xpath(".//tr[6]/td[6]/text()").get()
                object['Price/Sales (ttm)_12/31/2018'] = valuation.xpath(".//tr[6]/td[7]/text()").get()

                object['Price/Book (mrq)_current'] = valuation.xpath(".//tr[7]/td[2]/text()").get()
                object['Price/Book (mrq)_12/31/2019'] = valuation.xpath(".//tr[7]/td[3]/text()").get()
                object['Price/Book (mrq)_9/30/2019'] = valuation.xpath(".//tr[7]/td[4]/text()").get()
                object['Price/Book (mrq)_6/30/2019'] = valuation.xpath(".//tr[7]/td[5]/text()").get()
                object['Price/Book (mrq)_3/31/2019'] = valuation.xpath(".//tr[7]/td[6]/text()").get()
                object['Price/Book (mrq)_12/31/2018'] = valuation.xpath(".//tr[7]/td[7]/text()").get()

                object['Enterprise Value/Revenue_current'] = valuation.xpath(".//tr[8]/td[2]/text()").get()
                object['Enterprise Value/Revenue_12/31/2019'] = valuation.xpath(".//tr[8]/td[3]/text()").get()
                object['Enterprise Value/Revenue_9/30/2019'] = valuation.xpath(".//tr[8]/td[4]/text()").get()
                object['Enterprise Value/Revenue_6/30/2019'] = valuation.xpath(".//tr[8]/td[5]/text()").get()
                object['Enterprise Value/Revenue_3/31/2019'] = valuation.xpath(".//tr[8]/td[6]/text()").get()
                object['Enterprise Value/Revenue_12/31/2018'] = valuation.xpath(".//tr[8]/td[7]/text()").get()

                object['Enterprise Value/EBITDA_current'] = valuation.xpath(".//tr[9]/td[2]/text()").get()
                object['Enterprise Value/EBITDA_12/31/2019'] = valuation.xpath(".//tr[9]/td[3]/text()").get()
                object['Enterprise Value/EBITDA_9/30/2019'] = valuation.xpath(".//tr[9]/td[4]/text()").get()
                object['Enterprise Value/EBITDA_6/30/2019'] = valuation.xpath(".//tr[9]/td[5]/text()").get()
                object['Enterprise Value/EBITDA_3/31/2019'] = valuation.xpath(".//tr[9]/td[6]/text()").get()
                object['Enterprise Value/EBITDA_12/31/2018'] = valuation.xpath(".//tr[9]/td[7]/text()").get()



                # object['Enterprise Value']
                # object['Trailing P/E']
                # object['Forward P/E']
                # object['PEG Ratio (5 yr expected)']
                # object['Enterprise Value ']
                # object['Enterprise Value ']
                # object['Enterprise Value ']
                # object['Enterprise Value ']
            
            object['Levered free cash flow (ttm)'] = response.xpath("//*[@id='Col1-0-KeyStatistics-Proxy']/section/div[3]/div[3]/div/div[6]/div/div/table/tbody/tr[2]/td[2]/text()").get()

            # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[3]/div/div[6]/div/div/table/tbody/tr[2]/td[2]
            

            # with open('example.txt', 'a') as example: 
            #     example.write(response.text)

            # analysis_page = response.xpath("//a[@data-reactid='41']/@href").get()
            
            yield object

            # if analysis_page: 
            yield scrapy.Request(url='https://finance.yahoo.com/quote/{0}/analysis?p={0}'.format(last_chars), callback=self.parse_analysis)

    def parse_analysis(self, response): 
            object = {}

            last_chars = response.url.split('/')[4]
            print('response_url', response.url)
            print('last_chars', last_chars)

            object['stock_symbol'] = last_chars
            object['Next 5 years (per annum)'] = response.xpath("//*[@id='Col1-0-AnalystLeafPage-Proxy']/section/table[6]/tbody/tr[5]/td[2]/text()").get()

            yield object

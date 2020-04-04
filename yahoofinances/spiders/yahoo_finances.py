# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import time
import datetime


class YahooFinancesSpider(scrapy.Spider):
    name = 'yahoo_finances'
    # allowed_domains = ['finance.yahoo.com/quote']

    init_stock_sym = ['AAL', 'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'ALXN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ASML', 'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'BMRN', 'CDNS', 'CELG', 
                    'CERN', 'CHKP', 'CHTR', 'CMCSA', 'COST', 'CSCO', 'CSX', 'CTAS', 'CTRP', 'CTSH', 'CTXS', 'DLTR', 'EA', 'EBAY', 'EXPE', 'FAST', 'FB', 'FISV', 'FOX', 'FOXA', 'GILD', 
                    'GOOG', 'GOOGL', 'HAS', 'HSIC', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JBHT', 'JD', 'KHC', 'KLAC', 'LBTYA', 'LBTYK', 'LRCX', 'LULU', 'MAR', 'MCHP', 'MDLZ', 
                    'MELI', 'MNST', 'MSFT', 'MU', 'MXIM', 'MYL', 'NFLX', 'NTAP', 'NTES', 'NVDA', 'NXPI', 'ORLY', 'PAYX', 'PCAR', 'PEP', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SBUX', 'SIRI', 
                    'SNPS', 'SWKS', 'SYMC', 'TMUS', 'TSLA', 'TTWO', 'TXN', 'UAL', 'ULTA', 'VRSK', 'VRSN', 'VRTX', 'WBA', 'WDAY', 'WDC', 'WLTW', 'WYNN', 'XEL', 'XLNX']
    
    SandPplusNasdaq = ['DVA', 'ETFC', 'TFC', 'BBY', 'AMP', 'AVB', 'PNC', 'RSG', 'AVY', 'JCI', 'CRM', 'SBAC', 'BAX', 'CTSH', 'INCY', 'FDX', 'O', 'EQR', 'CMCSA', 'AMT', 'FLIR', 'UHS', 'PKI', 
                    'TSLA', 'IBM', 'PFG', 'QRVO', 'JPM', 'MO', 'LMT', 'TSN', 'NI', 'ZTS', 'CFG', 'SYMC', 'MSI', 'MSCI', 'RF', 'GOOG', 'BKNG', 'CSX', 'KLAC', 'LULU', 'BWA', 'ULTA', 'CXO', 
                    'AIG', 'PG', 'VRSN', 'GE', 'TJX', 'AKAM', 'XOM', 'C', 'FRC', 'SYK', 'CMS', 'CBRE', 'LW', 'DRE', 'TIF', 'BXP', 'AEE', 'ADM', 'GPC', 'RHI', 'XRAY', 'SYY', 'HSY', 'WRB', 
                    'COO', 'CVX', 'APTV', 'ARNC', 'NLSN', 'SEE', 'ISRG', 'MDT', 'GWW', 'ABBV', 'WAB', 'PNR', 'ASML', 'KHC', 'JNJ', 'UNM', 'BA', 'HLT', 'EMN', 'NVDA', 'MCK', 'GD', 'AAL', 
                    'FBHS', 'ESS', 'DISCA', 'MA', 'NOW', 'FITB', 'GM', 'LNT', 'WELL', 'SLG', 'KSU', 'IT', 'A', 'NWSA', 'UNH', 'ZBRA', 'PAYX', 'M', 'URI', 'VMC', 'SIRI', 'XYL', 'FLS', 
                    'MCD', 'ALK', 'EXPD', 'ALB', 'CINF', 'FTV', 'CHD', 'AXP', 'SNA', 'AFL', 'CCI', 'PHM', 'IRM', 'MTD', 'MAR', 'CF', 'DIS', 'DFS', 'EIX', 'HPQ', 'K', 'VNO', 'CAG', 'DOW', 
                    'IFF', 'RCL', 'MSFT', 'HBAN', 'AMCR', 'NCLH', 'XLNX', 'WAT', 'DGX', 'SIVB', 'AEP', 'HCA', 'PCAR', 'PSX', 'BDX', 'HAL', 'WBA', 'UPS', 'COF', 'LH', 'MHK', 'KEYS', 'ALGN', 
                    'BKR', 'FLT', 'PM', 'NOV', 'PNW', 'HES', 'IEX', 'LOW', 'NEM', 'SO', 'ADP', 'REG', 'CERN', 'FB', 'PWR', 'AVGO', 'TXN', 'QCOM', 'ALLE', 'USB', 'BMRN', 'MMM', 'ZBH', 'MS', 
                    'AMZN', 'VIAC', 'ECL', 'PPL', 'WDAY', 'NLOK', 'MU', 'V', 'CLX', 'FANG', 'WLTW', 'BR', 'NKE', 'NWL', 'EW', 'KO', 'KEY', 'WFC', 'LIN', 'AIV', 'RJF', 'ADBE', 'IPGP', 'ROL', 
                    'CPRI', 'DOV', 'SPGI', 'BRK-B', 'DRI', 'DE', 'EOG', 'CHRW', 'NBL', 'WMB', 'T', 'AOS', 'BLK', 'MXIM', 'VRSK', 'CB', 'TGT', 'WMT', 'ADSK', 'APA', 'AMGN', 'AMAT', 'WHR', 
                    'TXT', 'CNP', 'ICE', 'UNP', 'UAA', 'CTXS', 'ADS', 'PEG', 'MPC', 'AGN', 'ACN', 'WDC', 'FTI', 'OMC', 'AIZ', 'KR', 'CTL', 'DAL', 'CHKP', 'YUM', 'MGM', 'MELI', 'CNC', 'CVS', 
                    'CAT', 'PXD', 'DISH', 'HUM', 'MNST', 'PRU', 'HST', 'TTWO', 'AJG', 'IQV', 'WRK', 'OKE', 'TWTR', 'KMX', 'FOX', 'IVZ', 'VLO', 'CTVA', 'HBI', 'IDXX', 'RMD', 'ABC', 'OXY', 
                    'ANTM', 'MCO', 'WYNN', 'LNC', 'LB', 'VRTX', 'ABMD', 'LUV', 'COP', 'DHI', 'MMC', 'CI', 'NEE', 'GPS', 'MLM', 'PKG', 'COTY', 'ED', 'BSX', 'DTE', 'TSCO', 'SYF', 'SJM', 
                    'BEN', 'EXR', 'SWKS', 'VAR', 'AWK', 'KMB', 'HP', 'GOOGL', 'AAPL', 'NTAP', 'AME', 'TMUS', 'ROP', 'BK', 'DHR', 'ADI', 'KMI', 'TAP', 'AMD', 'J', 'INTU', 'DXC', 'TDG', 
                    'ARE', 'LHX', 'ATO', 'GILD', 'ORCL', 'WU', 'HAS', 'HFC', 'FIS', 'RTN', 'HOLX', 'HSIC', 'SWK', 'SCHW', 'CHTR', 'MET', 'RE', 'HIG', 'MKC', 'CPRT', 'EXC', 'PEP', 'FMC', 
                    'EL', 'COST', 'NSC', 'BIDU', 'PH', 'HRB', 'XEL', 'CBOE', 'PPG', 'AZO', 'JWN', 'INTC', 'LYB', 'PVH', 'NXPI', 'TROW', 'REGN', 'CL', 'ZION', 'NTRS', 'ABT', 'FE', 'BAC', 
                    'VFC', 'CDW', 'MRK', 'MCHP', 'HRL', 'CPB', 'BMY', 'TT', 'KSS', 'EFX', 'EQIX', 'LBTYA', 'ETN', 'PFE', 'PSA', 'LEN', 'CTRP', 'ANSS', 'XRX', 'SLB', 'ALXN', 'NDAQ', 'EXPE', 
                    'PEAK', 'JBHT', 'DLR', 'HD', 'WEC', 'ALL', 'CE', 'AES', 'TPR', 'HPE', 'NOC', 'PLD', 'FAST', 'CELG', 'D', 'NWS', 'GPN', 'PGR', 'TRV', 'FCX', 'PYPL', 'MRO', 'ATVI', 'ES', 
                    'GIS', 'FOXA', 'TMO', 'EA', 'VTR', 'NTES', 'FTNT', 'IP', 'APD', 'LYV', 'CDNS', 'IPG', 'EMR', 'UDR', 'GRMN', 'DUK', 'MKTX', 'MDLZ', 'PRGO', 'DLTR', 'L', 'WY', 'MYL', 
                    'AAP', 'AON', 'LRCX', 'FRT', 'NRG', 'FISV', 'SBUX', 'APH', 'JNPR', 'EVRG', 'F', 'UA', 'NVR', 'UTX', 'SHW', 'STT', 'TFX', 'GLW', 'LDOS', 'ITW', 'NUE', 'CSCO', 'BLL', 'LLY', 
                    'BF-B', 'UAL', 'IR', 'SRE', 'ETR', 'HII', 'WM', 'MOS', 'STX', 'EBAY', 'CAH', 'DD', 'ORLY', 'CCL', 'DG', 'ODFL', 'ROK', 'COG', 'HON', 'STE', 'ILMN', 'LKQ', 'GL', 'LEG', 
                    'VZ', 'LVS', 'CMG', 'GS', 'BIIB', 'STZ', 'CME', 'LBTYK', 'CTAS', 'HOG', 'JKHY', 'NFLX', 'CMA', 'MAA', 'SPG', 'ROST', 'FFIV', 'PBCT', 'RL', 'ANET', 'INFO', 'MAS', 'JD', 
                    'DISCK', 'MTB', 'DVN', 'PAYC', 'TEL', 'KIM', 'CMI', 'SNPS']

    final_url = []

    for stock in SandPplusNasdaq:
        final_url.append('https://finance.yahoo.com/quote/{0}?p={0}'.format(stock))


    start_urls = final_url

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

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%d/%m/%Y", named_tuple)

        now = datetime.datetime.utcnow()

        object['date'] = time_string

        object['utcdate'] = now

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

        object['Fair Value'] = response.xpath(
            "//div[@class='IbBox Ta(start) C($tertiaryColor)']/text()").get()
        object['Recommendation Rating'] = response.xpath(
            "//*[@id='Col2-7-QuoteModule-Proxy']/div/section/a/h2/span/text()").get()
        object['Undervalued or Overvalued'] = response.xpath("//*[@id='quote-summary']/div[3]/div[1]/div[2]/div[2]/text()").get()

        yield object

        # statistics_page = response.xpath("//*[@id='quote-nav']/ul/li[5]/a/@href").get()

        # if statistics_page:
        yield scrapy.Request(url='https://finance.yahoo.com/quote/{0}/key-statistics?p={0}'.format(last_chars), callback=self.parse_statistics)

    def parse_statistics(self, response):

        object = {}

        last_chars = response.url.split('/')[4]
        print('response_url', response.url)
        print('last_chars', last_chars)

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%d/%m/%Y", named_tuple)

        object['date'] = time_string

        object['stock_symbol'] = last_chars

        # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody

        # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[1]/td[2]

        # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[1]/td[3]

        # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]

        for valuation in response.xpath("//*[@id='Col1-0-KeyStatistics-Proxy']/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody"):
            print('valuation', valuation)

            object['Market Cap (intraday)_current'] = valuation.xpath(
                ".//tr[1]/td[2]/text()").get()
            object['Market Cap (intraday)_12/31/2019'] = valuation.xpath(
                ".//tr[1]/td[3]/text()").get()
            object['Market Cap (intraday)_9/30/2019'] = valuation.xpath(
                ".//tr[1]/td[4]/text()").get()
            object['Market Cap (intraday)_6/30/2019'] = valuation.xpath(
                ".//tr[1]/td[5]/text()").get()
            object['Market Cap (intraday)_3/31/2019'] = valuation.xpath(
                ".//tr[1]/td[6]/text()").get()
            object['Market Cap (intraday)_12/31/2018'] = valuation.xpath(
                ".//tr[1]/td[7]/text()").get()

            object['Enterprise Value_current'] = valuation.xpath(
                ".//tr[2]/td[2]/text()").get()
            object['Enterprise Value_12/31/2019'] = valuation.xpath(
                ".//tr[2]/td[3]/text()").get()
            object['Enterprise Value_9/30/2019'] = valuation.xpath(
                ".//tr[2]/td[4]/text()").get()
            object['Enterprise Value_6/30/2019'] = valuation.xpath(
                ".//tr[2]/td[5]/text()").get()
            object['Enterprise Value_3/31/2019'] = valuation.xpath(
                ".//tr[2]/td[6]/text()").get()
            object['Enterprise Value_12/31/2018'] = valuation.xpath(
                ".//tr[2]/td[7]/text()").get()

            object['Trailing P/E_current'] = valuation.xpath(
                ".//tr[3]/td[2]/text()").get()
            object['Trailing P/E_12/31/2019'] = valuation.xpath(
                ".//tr[3]/td[3]/text()").get()
            object['Trailing P/E_9/30/2019'] = valuation.xpath(
                ".//tr[3]/td[4]/text()").get()
            object['Trailing P/E_6/30/2019'] = valuation.xpath(
                ".//tr[3]/td[5]/text()").get()
            object['Trailing P/E_3/31/2019'] = valuation.xpath(
                ".//tr[3]/td[6]/text()").get()
            object['Trailing P/E_12/31/2018'] = valuation.xpath(
                ".//tr[3]/td[7]/text()").get()

            object['Forward P/E_current'] = valuation.xpath(
                ".//tr[4]/td[2]/text()").get()
            object['Forward P/E_12/31/2019'] = valuation.xpath(
                ".//tr[4]/td[3]/text()").get()
            object['Forward P/E_9/30/2019'] = valuation.xpath(
                ".//tr[4]/td[4]/text()").get()
            object['Forward P/E_6/30/2019'] = valuation.xpath(
                ".//tr[4]/td[5]/text()").get()
            object['Forward P/E_3/31/2019'] = valuation.xpath(
                ".//tr[4]/td[6]/text()").get()
            object['Forward P/E_12/31/2018'] = valuation.xpath(
                ".//tr[4]/td[7]/text()").get()

            object['PEG Ratio (5 yr expected)_current'] = valuation.xpath(
                ".//tr[5]/td[2]/text()").get()
            object['PEG Ratio (5 yr expected)_12/31/2019'] = valuation.xpath(
                ".//tr[5]/td[3]/text()").get()
            object['PEG Ratio (5 yr expected)_9/30/2019'] = valuation.xpath(
                ".//tr[5]/td[4]/text()").get()
            object['PEG Ratio (5 yr expected)_6/30/2019'] = valuation.xpath(
                ".//tr[5]/td[5]/text()").get()
            object['PEG Ratio (5 yr expected)_3/31/2019'] = valuation.xpath(
                ".//tr[5]/td[6]/text()").get()
            object['PEG Ratio (5 yr expected)_12/31/2018'] = valuation.xpath(
                ".//tr[5]/td[7]/text()").get()

            object['Price/Sales (ttm)_current'] = valuation.xpath(
                ".//tr[6]/td[2]/text()").get()
            object['Price/Sales (ttm)_12/31/2019'] = valuation.xpath(
                ".//tr[6]/td[3]/text()").get()
            object['Price/Sales (ttm)_9/30/2019'] = valuation.xpath(
                ".//tr[6]/td[4]/text()").get()
            object['Price/Sales (ttm)_6/30/2019'] = valuation.xpath(
                ".//tr[6]/td[5]/text()").get()
            object['Price/Sales (ttm)_3/31/2019'] = valuation.xpath(
                ".//tr[6]/td[6]/text()").get()
            object['Price/Sales (ttm)_12/31/2018'] = valuation.xpath(
                ".//tr[6]/td[7]/text()").get()

            object['Price/Book (mrq)_current'] = valuation.xpath(
                ".//tr[7]/td[2]/text()").get()
            object['Price/Book (mrq)_12/31/2019'] = valuation.xpath(
                ".//tr[7]/td[3]/text()").get()
            object['Price/Book (mrq)_9/30/2019'] = valuation.xpath(
                ".//tr[7]/td[4]/text()").get()
            object['Price/Book (mrq)_6/30/2019'] = valuation.xpath(
                ".//tr[7]/td[5]/text()").get()
            object['Price/Book (mrq)_3/31/2019'] = valuation.xpath(
                ".//tr[7]/td[6]/text()").get()
            object['Price/Book (mrq)_12/31/2018'] = valuation.xpath(
                ".//tr[7]/td[7]/text()").get()

            object['Enterprise Value/Revenue_current'] = valuation.xpath(
                ".//tr[8]/td[2]/text()").get()
            object['Enterprise Value/Revenue_12/31/2019'] = valuation.xpath(
                ".//tr[8]/td[3]/text()").get()
            object['Enterprise Value/Revenue_9/30/2019'] = valuation.xpath(
                ".//tr[8]/td[4]/text()").get()
            object['Enterprise Value/Revenue_6/30/2019'] = valuation.xpath(
                ".//tr[8]/td[5]/text()").get()
            object['Enterprise Value/Revenue_3/31/2019'] = valuation.xpath(
                ".//tr[8]/td[6]/text()").get()
            object['Enterprise Value/Revenue_12/31/2018'] = valuation.xpath(
                ".//tr[8]/td[7]/text()").get()

            object['Enterprise Value/EBITDA_current'] = valuation.xpath(
                ".//tr[9]/td[2]/text()").get()
            object['Enterprise Value/EBITDA_12/31/2019'] = valuation.xpath(
                ".//tr[9]/td[3]/text()").get()
            object['Enterprise Value/EBITDA_9/30/2019'] = valuation.xpath(
                ".//tr[9]/td[4]/text()").get()
            object['Enterprise Value/EBITDA_6/30/2019'] = valuation.xpath(
                ".//tr[9]/td[5]/text()").get()
            object['Enterprise Value/EBITDA_3/31/2019'] = valuation.xpath(
                ".//tr[9]/td[6]/text()").get()
            object['Enterprise Value/EBITDA_12/31/2018'] = valuation.xpath(
                ".//tr[9]/td[7]/text()").get()

            # object['Enterprise Value']
            # object['Trailing P/E']
            # object['Forward P/E']
            # object['PEG Ratio (5 yr expected)']
            # object['Enterprise Value ']
            # object['Enterprise Value ']
            # object['Enterprise Value ']
            # object['Enterprise Value ']

        object['Levered free cash flow (ttm)'] = response.xpath(
            "//*[@id='Col1-0-KeyStatistics-Proxy']/section/div[3]/div[3]/div/div[6]/div/div/table/tbody/tr[2]/td[2]/text()").get()

        object['Total Cash (mrq)'] = response.xpath("//*[@id='Col1-0-KeyStatistics-Proxy']/section/div[3]/div[3]/div/div[5]/div/div/table/tbody/tr[1]/td[2]/text()").get()

        object['Shares Outstanding'] = response.xpath("//*[@id='Col1-0-KeyStatistics-Proxy']/section/div[3]/div[2]/div/div[2]/div/div/table/tbody/tr[3]/td[2]/text()").get()

        # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[3]/div/div[6]/div/div/table/tbody/tr[2]/td[2]

        # with open('example.txt', 'a') as example:
        #     example.write(response.text)

        # analysis_page = response.xpath("//a[@data-reactid='41']/@href").get()

        yield object

        # if analysis_page:
        yield scrapy.Request(url='https://finance.yahoo.com/quote/{0}/analysis?p={0}'.format(last_chars), callback=self.parse_analysis)

    def parse_analysis(self, response):
        object = {}

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%d/%m/%Y", named_tuple)

        object['date'] = time_string

        last_chars = response.url.split('/')[4]
        print('response_url', response.url)
        print('last_chars', last_chars)

        object['stock_symbol'] = last_chars
        object['Next 5 years (per annum)'] = response.xpath(
            "//*[@id='Col1-0-AnalystLeafPage-Proxy']/section/table[6]/tbody/tr[5]/td[2]/text()").get()

        yield object

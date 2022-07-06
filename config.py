# логирование
LOG_PATH = 'logs/investing_test.log'
LOG_FORMAT = '%(name)s - %(levelname)s - %(message)s'
SCREENSHOTS_PATH = 'screenshots'


# элементы для поиска
URL = 'https://ru.investing.com'

XPATH_markets = '/html/body/div[4]/header/div[2]/nav[1]/ul/li[1]/a'
XPATH_markets_equities = '/html/body/div[4]/header/div[2]/nav[1]/ul/li[1]/ul/li[4]/a'
XPATH_markets_equities_russia = '/html/body/div[4]/header/div[2]/nav[1]/ul/li[1]/ul/li[4]/div/ul[1]/li[3]/a'

XPATH_stocks_filter_dropdown = '//*[@id="stocksFilter"]'
XPATH_stocksFilter_all = '//*[@id="all"]'

XPATH_table_rows = '/html/body/div[4]/section/div[8]/div/table/tbody/tr'

XPATH_table_market_stocks = '//*[@id="cross_rate_markets_stocks_1"]'

XPATH_stock_name = '/html/body/div/div[2]/div/div/div[2]/main/div/div[1]/div[1]/h1'
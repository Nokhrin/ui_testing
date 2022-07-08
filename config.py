# логирование
SCREENSHOTS_DIRECTORY = 'screenshots'


# элементы для поиска
URL = 'https://ru.investing.com'

XPATH_markets = '/html/body/div[4]/header/div[2]/nav[1]/ul/li[1]/a'
XPATH_markets_equities = '/html/body/div[4]/header/div[2]/nav[1]/ul/li[1]/ul/li[4]/a'
XPATH_markets_equities_russia = '/html/body/div[4]/header/div[2]/nav[1]/ul/li[1]/ul/li[4]/div/ul[1]/li[3]/a'

XPATH_stocks_filter_dropdown = '//*[@id="stocksFilter"]'
XPATH_stocksFilter_all = '//*[@id="all"]'

XPATH_table_results = '/html/body/div[4]/section/div[8]/div/table'
XPATH_table_rows = '//*[@id="cross_rate_markets_stocks_1"]/tbody/tr'
# XPATH_table_rows = '/html/body/div[4]/section/div[8]/div/table/tbody/tr'

XPATH_table_market_stocks = '//*[@id="cross_rate_markets_stocks_1"]'

XPATH_all_stocks_links = '//*[@id="cross_rate_markets_stocks_1"]/tbody/tr*/*[2]/a'

XPATH_stock_name = '/html/body/div/div[2]/div/div/div[2]/main/div/div[1]/div[1]/h1'

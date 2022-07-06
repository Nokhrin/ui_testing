import config
import random

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = config.URL

        super().__init__(web_driver, url)

    #
    markets_link = WebElement(xpath=config.XPATH_markets)

    #
    markets_equities_link = WebElement(xpath=config.XPATH_markets_equities)

    #
    markets_equities_russia_link = WebElement(xpath=config.XPATH_markets_equities_russia)

    #
    stocks_filter_dropdown = WebElement(xpath=config.XPATH_stocks_filter_dropdown)

    #
    full_table_rows = ManyWebElements(xpath=config.XPATH_table_rows)

    #
    stocks_table = WebElement(xpath=config.XPATH_table_market_stocks)

    #
    def get_random_cell(self, random_cell_xpath):
        """ Вернуть вторую ячейку случайно выбранной строки """

        random_second_cell = WebElement(xpath=random_cell_xpath)

        return random_second_cell

    def get_random_stock(self, random_xpath):
        """ Вернуть ссылку из второго столбца случайно выбранной строки """

        random_stock = WebElement(xpath=random_xpath)

        return random_stock

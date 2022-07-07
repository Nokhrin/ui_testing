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
    table_results = WebElement(xpath=config.XPATH_table_results)

    #
    full_table_rows = ManyWebElements(xpath=config.XPATH_table_rows)

    #
    stocks_table = WebElement(xpath=config.XPATH_table_market_stocks)


    def get_element_by_xpath(self, element_xpath):
        """ Вернуть ссылку из второго столбца случайно выбранной строки """
        # element = WebElement(xpath="//*[@id=\"pair_1171256\"]/td[2]/a")
        print('зашли в метод')
        # print(self)
        # print(element_xpath)
        # print(self.WebElement(xpath=element_xpath))
        # print(self.WebElement(xpath=element_xpath).get_attribute('title'))
        print('выходим из метода')
        self.new_element = WebElement(xpath=element_xpath)

    # get_element_by_xpath.add_element

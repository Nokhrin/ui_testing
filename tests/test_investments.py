import pytest
import config
from pages.investments import MainPage
import time
import random
from datetime import datetime


def test_check_main_search(web_browser):
    # 1. Зайти на сайт https://ru.investing.com
    page = MainPage(web_browser)

    # 2. Перейти в меню "Котировки" -> "Акции" -> "Россия".
    page.markets_link.mouse_hover(hold_seconds=2)

    page.markets_equities_link.mouse_hover(hold_seconds=2)

    page.markets_equities_russia_link.click()

    # 3. В выпадающем меню с типами акций выбрать "Россия - все акции"
    page.wait_page_loaded()

    page.stocks_filter_dropdown.select_option(option_index=0)

    # 4. Выбрать случайную акцию в таблице со списком акций
    print(f'\nвсего строк: {page.full_table_rows.count()}')
    random_stock_row_number = random.randint(0, (page.full_table_rows.count() - 1))
    print(f'выбрали строку: {random_stock_row_number}')
    selected_stock_link_XPATH = f'/html/body/div[4]/section/div[8]/div/table/tbody/tr[{random_stock_row_number}]/td[2]/a'

    random_stock_link = page.get_random_stock(random_xpath=selected_stock_link_XPATH)

    page.wait_page_loaded(check_page_changes=True, sleep_time=15)


    # 5. Навести курсор мыши на название выбранной акции
    # random_stock_link.mouse_hover(x_offset=0, y_offset=0, hold_seconds=5)

    # 6. Сохранить название акции, отображающееся в всплывающей подсказке
    random_stock_title = random_stock_link.get_attribute('title')
    print(random_stock_title)

    # 7. Нажать на выбранную акцию для перехода в детальное описание
    random_stock_link.click()

    # 8. Проверить совпадение названия акций на странице детального описания с сохраненным названием.


    # # снимок финальной страницы
    # url_to_screenshot = page.get_current_url()
    # # создать уникальное имя для снимка
    # time_stamp = datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    # split_position = url_to_screenshot.rfind('/')
    # screenshot_filename = f'{url_to_screenshot[split_position:]}_{time_stamp}.png'
    # screenshot_fullname = f'{config.SCREENSHOTS_PATH}{screenshot_filename}'
    # page.screenshot(file_name=screenshot_fullname)

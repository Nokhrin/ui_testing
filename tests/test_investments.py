import pytest
import config
from pages.investments import MainPage
import time
import random
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_check_main_search(web_browser):
    action = ActionChains(web_browser)

    # 1. Зайти на сайт https://ru.investing.com
    page = MainPage(web_browser)

    # 2. Перейти в меню "Котировки" -> "Акции" -> "Россия".
    page.markets_link.mouse_hover(hold_seconds=1)

    page.markets_equities_link.mouse_hover(hold_seconds=1)

    page.markets_equities_russia_link.click()

    # 3. В выпадающем меню с типами акций выбрать "Россия - все акции"
    page.stocks_filter_dropdown.scroll_element_into_view()
    page.stocks_filter_dropdown.select_option(option_index=0)

    # 4. Выбрать случайную акцию в таблице со списком акций

    # таблица результатов
    # page.table_results.scroll_element_into_view()

    print(f'\nвсего строк: {page.full_table_rows.count()}')
    random_stock_row_number = random.randint(0, (page.full_table_rows.count() - 1))
    print(f'выбрали строку: {random_stock_row_number}')

    # абсолютный xpath
    selected_stock_link_XPATH = f'/html/body/div[4]/section/div[8]/div/table/tbody/tr[{random_stock_row_number}]/td[2]/a'

    # относительный xpath ссылки - //*[@id="pair_13725"]/td[2]/a
    # selected_stock_link_XPATH = f'//*[@id="{row_identifier}"]/td[2]/a'

    random_stock_link = web_browser.find_element(By.XPATH, selected_stock_link_XPATH)

    # title = random_stock_link.get_attribute('title')
    # print(title)

    # 5. Навести курсор мыши на название выбранной акции
    # random_stock_link.mouse_hover(x_offset=0, y_offset=0, hold_seconds=5)
    action.move_to_element(random_stock_link).perform()

    # 6. Сохранить название акции, отображающееся в всплывающей подсказке
    random_stock_title = random_stock_link.get_attribute('title')
    print(f'random_stock_title: {random_stock_title}')

    # 7. Нажать на выбранную акцию для перехода в детальное описание
    random_stock_link.click()

    # 8. Проверить совпадение названия акций на странице детального описания с сохраненным названием.
    print(f'поиск наименования: {config.XPATH_stock_name}')
    # logging.info(f'поиск наименования: {config.XPATH_stock_name}')

    stock_detailed_name = web_browser.find_element(By.XPATH, config.XPATH_stock_name)

    print(f'детальное наименование: {stock_detailed_name.text}')
    # logging.info(f'детальное наименование: {stock_detailed_name.text}')

    # подготовка наименования для сравнения
    split_position = stock_detailed_name.text.rfind('(')
    stock_name = stock_detailed_name.text[:split_position].strip()

    # logging.info(f'детальное наименование подготовленное: {stock_name}')

    # сравнение наименований
    if random_stock_title.lower() == stock_name.lower():
        print(f'названия совпадают')
        # logging.info(f'названия совпадают')
    else:
        print(f'названия различаются')
        # logging.info(f'названия различаются')


    # снимок финальной страницы
    url_to_screenshot = page.get_current_url()
    # создать уникальное имя для снимка
    time_stamp = datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    split_position = url_to_screenshot.rfind('/')
    screenshot_filename = f'{url_to_screenshot[split_position:]}_{time_stamp}.png'
    screenshot_fullname = f'{config.SCREENSHOTS_DIRECTORY}{screenshot_filename}'
    page.screenshot(file_name=screenshot_fullname)

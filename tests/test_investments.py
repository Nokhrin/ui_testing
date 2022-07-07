import pytest
import config
from pages.investments import MainPage
import time
import random
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import logging
logger = logging.getLogger(__name__)

def test_check_main_search(web_browser):
    logger.info('тест стартовал')

    action = ActionChains(web_browser)

    # 1. Зайти на сайт https://ru.investing.com
    page = MainPage(web_browser)
    logger.info('главная страница загружена')

    # 2. Перейти в меню "Котировки" -> "Акции" -> "Россия"
    logger.info(f'поиск элемента: {config.XPATH_markets}')
    page.markets_link.mouse_hover(hold_seconds=1)
    logger.info(f'выполнено наведение на пункт "Котировки"')

    logger.info(f'поиск элемента: {config.XPATH_markets_equities}')
    page.markets_equities_link.mouse_hover(hold_seconds=1)
    logger.info(f'выполнено наведение на пункт "Котировки" -> "Акции"')

    logger.info(f'поиск элемента: {config.XPATH_markets_equities_russia}')
    page.markets_equities_russia_link.click()
    logger.info(f'выполнено нажатие на пункт "Котировки" -> "Акции" -> "Россия"')

    # 3. В выпадающем меню с типами акций выбрать "Россия - все акции"
    logger.info(f'поиск элемента: {config.XPATH_stocks_filter_dropdown}')
    page.stocks_filter_dropdown.scroll_element_into_view()

    logger.info(f'выбор опции: {config.XPATH_stocks_filter_dropdown}')
    page.stocks_filter_dropdown.select_option(option_index=0)
    logger.info(f'в выпадающем меню выбран пункт "Россия - все акции"')

    # 4. Выбрать случайную акцию в таблице со списком акций

    # таблица результатов
    logger.info(f'обработка таблицы: {config.XPATH_stocks_filter_dropdown}')
    logger.info(f'\nвыбор случайной акции:')
    logger.info(f'\n\tвсего строк: {page.full_table_rows.count()}')
    random_stock_row_number = random.randint(0, (page.full_table_rows.count() - 1))
    logger.info(f'\n\tвыбрали строку № {random_stock_row_number}')
    logger.info(f'x-path: {config.XPATH_stocks_filter_dropdown}')
    # абсолютный xpath
    selected_stock_link_XPATH = f'/html/body/div[4]/section/div[8]/div/table/tbody/tr[{random_stock_row_number}]/td[2]/a'

    # относительный xpath ссылки - пример - //*[@id="pair_13725"]/td[2]/a
    # selected_stock_link_XPATH = f'//*[@id="{row_identifier}"]/td[2]/a'

    logger.info(f'поиск элемента: {selected_stock_link_XPATH}')
    random_stock_link = web_browser.find_element(By.XPATH, selected_stock_link_XPATH)
    random_stock_title = random_stock_link.get_attribute('title')
    logger.info(f'в строке {random_stock_row_number} обнаружена ссылка на акции "{random_stock_title}"')

    # 5. Навести курсор мыши на название выбранной акции
    action.move_to_element(random_stock_link).perform()
    logger.info(f'курсор наведен на "{random_stock_title}"')

    # 6. Сохранить название акции, отображающееся в всплывающей подсказке
    logger.info(f'сохранено название акции, отображающееся в всплывающей подсказке: {random_stock_title}')

    # 7. Нажать на выбранную акцию для перехода в детальное описание
    random_stock_link.click()
    logger.info(f'произведено нажатие на "{random_stock_title}"')
    page.wait_page_loaded()

    # 8. Проверить совпадение названия акций на странице детального описания с сохраненным названием
    logger.info(f'x-path {selected_stock_link_XPATH}')
    stock_detailed_header = web_browser.find_element(By.XPATH, config.XPATH_stock_name)
    # stock_detailed_header = WebElement('x-path', config.XPATH_stock_name)
    # stock_detailed_header.scroll_to_element() # прокрутка до названия
    logger.info(f'наименование на странице детального описания: "{stock_detailed_header.text}"')

    # подготовка наименования для сравнения
    split_position = stock_detailed_header.text.rfind('(')
    stock_name = stock_detailed_header.text[:split_position].strip()
    logger.info(f'детальное наименование подготовленное: "{stock_name}"')

    # сравнение наименований
    if random_stock_title.lower() == stock_name.lower():
        logger.info(f'названия совпадают')
    else:
        logger.info(f'названия различаются')


    # снимок финальной страницы
    url_to_screenshot = page.get_current_url()
    # создать уникальное имя для снимка
    time_stamp = datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    split_position = url_to_screenshot.rfind('/')
    screenshot_filename = f'{url_to_screenshot[split_position:]}_{time_stamp}.png'
    screenshot_fullname = f'{config.SCREENSHOTS_DIRECTORY}{screenshot_filename}'
    page.screenshot(file_name=screenshot_fullname)
    logger.info(f'снимок страницы {url_to_screenshot} сохранен в файл {screenshot_fullname}')

    # провальный тест - для проверки
    # assert random_stock_title.lower() == stock_detailed_header.text.lower()
    # предположительно положительный тест
    assert random_stock_title.lower() == stock_name.lower()

    logger.info('выполнение теста завершено')

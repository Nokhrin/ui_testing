Установка и запуск теста:
1. Загрузить необходимый драйвер в директорию drivers
драйверы для Google Chrome: https://chromedriver.chromium.org/downloads
драйверы для Firefox: https://github.com/mozilla/geckodriver/releases

2. Установить зависимости:
python -m pip install -r requirements.txt

3. Файл config.py содержит переменные:
    - директория скриншотов
    - стартовая страница
    - локаторы элементов

4. Файл pytest.ini содержит настройки логирования

5. Для запуска в headless режиме в модуле conftest раскомментировать строку в фикстурах
chrome_options.add_argument('--headless') или firefox_options.add_argument('--headless')
!!! работа в headless режиме не отлажена

6. Запуск теста:
в Google Chrome:
python -m pytest --driver Chrome --driver-path drivers/chromedriver

в Firefox:
!!! работа не отлажена
python -m pytest --driver Firefox --driver-path drivers/geckodriver


!!! замечание
На моей машине штатно отрабатывает только
python -m pytest --driver Chrome --driver-path drivers/chromedriver
При этом примерно один из пяти раз вылетает с ошибкой драйвера на самом первом шаге.

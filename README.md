Установка и запуск теста:
 1) Загрузить необходимый драйвер в директорию drivers
    драйверы для Google Chrome: https://chromedriver.chromium.org/downloads
 2) Установить зависимости:
    pip install -r requirements.txt
 3) Запуск теста:
    python3 -m pytest -v --driver Chrome --driver-path drivers/chromedriver


Для запуска в headless режиме раскомментировать строку chrome_options.add_argument('--headless') в модуле conftest.
!!! работа в headless режиме не отлажена


python -m pytest -s --driver Chrome --driver-path drivers/chromedriver
python -m pytest -s --driver Firefox --driver-path drivers/geckodriver

from selenium.webdriver.chrome.service import Service
from pages.locators import Locators
from selenium import webdriver
from config import PATH
import pytest


@pytest.fixture()
def browser():
    """
    Функция для инициализации браузера
    """
    # Режим тестирования без открытия браузера Google Chrome
    service = Service(PATH)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

    # Режим тестирования с открытием браузера Google Chrome
    # driver = Service(PATH)
    # driver = webdriver.Chrome(service=driver)
    # driver.maximize_window()
    # yield driver
    # driver.quit()


@pytest.fixture()
def auth(browser):
    """
    Функция для авторизации
    """
    auth = Locators(browser)
    return auth
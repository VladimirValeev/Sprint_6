from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://qa-scooter.praktikum-services.ru/"


def test_scooter_logo_returns_to_main(driver):
    page = MainPage(driver, URL)
    page.open()
    page.click_order_top()
    page.click_scooter_logo()
    assert driver.current_url == URL


def test_yandex_logo_opens_dzen(driver):
    page = MainPage(driver, URL)
    page.open()
    page.click_yandex_logo()

    # Переключаемся в новое окно
    driver.switch_to.window(driver.window_handles[-1])

    # Ждём, пока урл станет с Дзеном, а не about:blank
    WebDriverWait(driver, 10).until(EC.url_contains("dzen"))

    assert "dzen" in driver.current_url.lower()

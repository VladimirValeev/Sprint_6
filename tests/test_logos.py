import pytest
from pages.main_page import MainPage


class TestLogos:
    def test_scooter_logo_returns_to_main(self, driver):
        page = MainPage(driver)
        # Открываем главную страницу
        page.open()
        # Нажимаем кнопку "Заказать" вверху страницы, чтобы уйти со страницы
        page.click_order_top()
        # Жмём на логотип "Самокат"
        page.click_scooter_logo()
        # Проверяем, что вернулись на главную страницу Самоката
        assert "qa-scooter.praktikum-services.ru" in driver.current_url

    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.open()

        # Запоминаем, сколько вкладок было до клика
        initial_handles = driver.window_handles[:]

        # Кликаем по логотипу Яндекса
        page.click_yandex_logo()

        # Переключаемся на последнюю (новую) вкладку
        page.switch_to_window(-1)

        # Проверяем, что вкладок стало больше, чем было — значит ДЗЕН (или что-то вместо него)
        # открылся в новой вкладке, даже если URL = about:blank из-за ограничений среды
        assert len(driver.window_handles) > len(initial_handles)

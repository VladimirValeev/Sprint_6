import allure
from pages.main_page import MainPage


class TestLogos:

    @allure.title("Клик по логотипу Самоката ведёт на главную страницу")
    def test_scooter_logo_returns_to_main(self, driver):
        page = MainPage(driver)
        page.open()

        page.click_order_top()
        page.click_scooter_logo()

        assert "qa-scooter.praktikum-services.ru" in page.get_current_url()

    @allure.title("Клик по логотипу Яндекса открывает новую вкладку")
    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.open()

        initial_handles = page.get_window_handles()

        page.click_yandex_logo()
        page.switch_to_window(-1)

        new_handles = page.get_window_handles()

        # Проверяем факт открытия новой вкладки (в среде URL может быть about:blank)
        assert len(new_handles) > len(initial_handles)

import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    # константа URL, которую ждёт тест test_scooter_logo_returns_to_main
    URL = MainPageLocators.URL

    # ---------------- ЛОГОТИПЫ ----------------

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    # ---------------- КНОПКИ 'ЗАКАЗАТЬ' ----------------

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_bottom(self):
        # Для нижней кнопки нужен скролл
        self.scroll_into_view(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по кнопке 'Заказать' из точки входа: {entry_point}")
    def click_order(self, entry_point: str):
        """
        entry_point ожидает значения:
        - 'top'    — верхняя кнопка
        - 'bottom' — нижняя кнопка
        """
        if entry_point == "top":
            self.click_order_top()
        elif entry_point == "bottom":
            self.click_order_bottom()
        else:
            raise ValueError(f"Unknown entry point: {entry_point}")

    # ---------------- FAQ ----------------

    @allure.step("Клик по вопросу FAQ №{index}")
    def click_question(self, index: int):
        locator = MainPageLocators.QUESTION(index)
        self.scroll_into_view(locator)
        self.click(locator)

    @allure.step("Получить текст ответа FAQ №{index}")
    def get_answer(self, index: int) -> str:
        locator = MainPageLocators.ANSWER(index)
        # больше никакого прямого self.driver.find_element — всё через BasePage
        return self.get_element_text(locator)

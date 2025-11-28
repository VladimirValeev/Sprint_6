from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def click_question(self, index):
        self.click(MainPageLocators.QUESTION(index))

    def get_answer(self, index):
        return self.text(MainPageLocators.ANSWER(index))

    def click_order_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

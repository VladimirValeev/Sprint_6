import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить имя: {first}")
    def set_first_name(self, first: str):
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, first)

    @allure.step("Заполнить фамилию: {last}")
    def set_last_name(self, last: str):
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last)

    @allure.step("Заполнить адрес: {address}")
    def set_address(self, address: str):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Выбрать станцию метро: {metro}")
    def select_metro(self, metro: str):
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(OrderPageLocators.METRO_DROPDOWN_OPTION(metro))

    @allure.step("Заполнить телефон: {phone}")
    def set_phone(self, phone: str):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Перейти на шаг 'Про аренду'")
    def go_to_rent_step(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Установить дату: {date}")
    def set_date(self, date: str):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        self.press_enter(OrderPageLocators.DATE_INPUT)

    @allure.step("Выбрать срок аренды: {period}")
    def select_rental_period(self, period: str):
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENTAL_PERIOD_OPTION(period))

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color: str):
        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)

    @allure.step("Заполнить комментарий: {comment}")
    def set_comment(self, comment: str):
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Отправить заказ")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.YES_BUTTON)

    @allure.step("Получить текст окна 'Заказ оформлен'")
    def get_success_modal_text(self) -> str:
        return self.get_element_text(OrderPageLocators.CONFIRM_TITLE, timeout=20)

    # ---------- Сборные шаги ----------

    @allure.step("Заполнить данные клиента")
    def fill_customer_info(self, first, last, address, metro, phone):
        self.set_first_name(first)
        self.set_last_name(last)
        self.set_address(address)
        self.select_metro(metro)
        self.set_phone(phone)

    @allure.step("Заполнить данные аренды")
    def fill_rent_info(self, date, rental_period, color, comment):
        self.set_date(date)
        self.select_rental_period(rental_period)
        self.select_color(color)
        self.set_comment(comment)

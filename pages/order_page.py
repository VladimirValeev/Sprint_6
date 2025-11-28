from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_first_step(self, first_name, last_name, address, metro, phone):
        # Имя, фамилия, адрес
        self.write(OrderPageLocators.FIRST_NAME, first_name)
        self.write(OrderPageLocators.LAST_NAME, last_name)
        self.write(OrderPageLocators.ADDRESS, address)

        # Станция метро
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(OrderPageLocators.METRO_OPTION(metro))

        # Телефон
        self.write(OrderPageLocators.PHONE, phone)

        # Кнопка Далее
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_step(self, date_day, rent_period, color, comment):
        # Дата
        self.click(OrderPageLocators.DATE_INPUT)
        self.click(OrderPageLocators.DATE_DAY(date_day))

        # Срок аренды
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.RENT_OPTION(rent_period))

        # Цвет самоката
        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)

        # Комментарий
        if comment:
            self.write(OrderPageLocators.COMMENT, comment)

        # Подтверждение заказа
        self.click(OrderPageLocators.FINAL_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def wait_for_success_modal(self) -> str:
        return self.text(OrderPageLocators.SUCCESS_MODAL_HEADER)

    def is_order_success(self) -> bool:
        header_text = self.wait_for_success_modal()
        return "Заказ оформлен" in header_text

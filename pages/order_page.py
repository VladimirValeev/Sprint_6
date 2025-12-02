import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """
    Страница оформления заказа:
    - шаг 1: данные клиента
    - шаг 2: про аренду
    """

    # ----------------- Вспомогательные методы -----------------

    def _click(self, locator):
        """Клик по элементу с ожиданием кликабельности и скроллом к нему."""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def _type(self, locator, text, clear=True):
        """Ввод текста в поле с ожиданием видимости."""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        if clear:
            element.clear()
        element.send_keys(text)

    # ----------------- Шаг 1: Данные клиента -----------------

    @allure.step("Ввести имя: {first}")
    def set_first_name(self, first):
        self._type(OrderPageLocators.FIRST_NAME_INPUT, first)

    @allure.step("Ввести фамилию: {last}")
    def set_last_name(self, last):
        self._type(OrderPageLocators.LAST_NAME_INPUT, last)

    @allure.step("Ввести адрес: {address}")
    def set_address(self, address):
        self._type(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Выбрать станцию метро: {metro}")
    def select_metro(self, metro):
        self._click(OrderPageLocators.METRO_INPUT)
        self._click(OrderPageLocators.METRO_DROPDOWN_OPTION(metro))

    @allure.step("Ввести телефон: {phone}")
    def set_phone(self, phone):
        self._type(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Заполнить данные клиента")
    def fill_customer_info(self, first, last, address, metro, phone):
        self.set_first_name(first)
        self.set_last_name(last)
        self.set_address(address)
        self.select_metro(metro)
        self.set_phone(phone)

    @allure.step("Перейти на шаг 'Про аренду'")
    def go_to_rent_step(self):
        self._click(OrderPageLocators.NEXT_BUTTON)

    # ----------------- Шаг 2: Про аренду -----------------

    @allure.step("Указать дату: {date}")
    def set_date(self, date):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT)
        )
        element.clear()
        element.send_keys(date + "\n")

    @allure.step("Выбрать срок аренды: {period}")
    def select_rental_period(self, period):
        self._click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self._click(OrderPageLocators.RENTAL_PERIOD_OPTION(period))

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self._click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self._click(OrderPageLocators.COLOR_GREY)

    @allure.step("Ввести комментарий: {comment}")
    def set_comment(self, comment):
        if comment:
            self._type(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Заполнить данные об аренде")
    def fill_rental_info(self, date, rental_period, color, comment):
        self.set_date(date)
        self.select_rental_period(rental_period)
        self.select_color(color)
        self.set_comment(comment)

    # ТЕСТ вызывает именно этот метод: fill_rent_info
    def fill_rent_info(self, date, rental_period, color, comment):
        return self.fill_rental_info(date, rental_period, color, comment)

    # ----------------- Подтверждение заказа -----------------

    @allure.step("Нажать кнопку 'Заказать'")
    def submit_order(self):
        self._click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self._click(OrderPageLocators.YES_BUTTON)

    @allure.step("Ожидать появления окна 'Заказ оформлен'")
    def wait_order_confirm(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(OrderPageLocators.CONFIRM_TITLE)
        )

    @allure.step("Получить текст модального окна 'Заказ оформлен'")
    def get_success_modal_text(self):
        """
        Ждём модалку 'Хотите оформить заказ?' → жмём 'Да' (если есть),
        затем ждём модалку с заголовком (Order_ModalHeader) и возвращаем её текст.
        """
        # сначала пробуем нажать "Да" (если модалка подтверждения есть)
        try:
            self._click(OrderPageLocators.YES_BUTTON)
        except TimeoutException:
            # если модалки с "Да" нет — идём дальше
            pass

        modal = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(OrderPageLocators.CONFIRM_TITLE)
        )
        return modal.text

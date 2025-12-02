# tests/test_order.py
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


ORDER_DATA = [
    (
        "top",
        "Иван",
        "Иванов",
        "Москва, Ленина 5",
        "Сокольники",
        "+79990000001",
        "15.12.2025",
        "сутки",
        "black",
        "Позвонить за час",
    ),
    (
        "bottom",
        "Пётр",
        "Петров",
        "Москва, Арбат 1",
        "Арбатская",
        "+79990000002",
        "20.12.2025",
        "двое суток",
        "grey",
        "Можно без звонка",
    ),
]


class TestOrder:

    @pytest.mark.parametrize(
        "entry_point, first_name, last_name, address, metro, phone, date, rental_period, color, comment",
        ORDER_DATA,
    )
    def test_order_success(
        self,
        driver,
        entry_point,
        first_name,
        last_name,
        address,
        metro,
        phone,
        date,
        rental_period,
        color,
        comment,
    ):
        main_page = MainPage(driver)
        main_page.open()

        if entry_point == "top":
            main_page.click_order_top()
        else:
            main_page.click_order_bottom()

        order_page = OrderPage(driver, driver.current_url)

        order_page.fill_customer_info(first_name, last_name, address, metro, phone)
        order_page.go_to_rent_step()
        order_page.fill_rent_info(date, rental_period, color, comment)
        order_page.submit_order()

        success_text = order_page.get_success_modal_text()

        assert "Заказ оформлен" in success_text

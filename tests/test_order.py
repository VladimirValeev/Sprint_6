import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage


# Тестовые данные для оформления заказа
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

    @allure.title("Успешное оформление заказа через верхнюю и нижнюю кнопки 'Заказать'")
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

        # Выбор точки входа в заказ — внутри PageObject, без if в тесте
        main_page.click_order(entry_point)

        # Открылась форма заказа
        order_page = OrderPage(driver, main_page.get_current_url())

        # Шаг 1: данные клиента
        order_page.fill_customer_info(first_name, last_name, address, metro, phone)

        # Переход на шаг аренды
        order_page.go_to_rent_step()

        # Шаг 2: параметры аренды
        order_page.fill_rent_info(date, rental_period, color, comment)

        # Отправляем заказ и подтверждаем
        order_page.submit_order()

        # Проверяем, что появилось модальное окно с подтверждением
        success_text = order_page.get_success_modal_text()
        assert "Заказ оформлен" in success_text

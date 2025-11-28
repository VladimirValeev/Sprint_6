import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@pytest.mark.parametrize(
    "order_button, first_name, last_name, address, metro, phone, day, rent, color, comment",
    [
        (
            "top",
            "Иван",
            "Иванов",
            "Москва, Ленина 5",
            "Сокольники",
            "+79990000001",
            "15",
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
            "20",
            "двое суток",
            "grey",
            "Можно без звонка",
        ),
    ],
)
def test_order_success(
    driver,
    order_button,
    first_name,
    last_name,
    address,
    metro,
    phone,
    day,
    rent,
    color,
    comment,
):
    main_page = MainPage(driver, BASE_URL)
    main_page.open()

    # Выбираем кнопку заказа: верхняя или нижняя
    if order_button == "top":
        main_page.click_order_top()
    else:
        main_page.click_order_bottom()

    order_page = OrderPage(driver)

    order_page.fill_first_step(first_name, last_name, address, metro, phone)
    order_page.fill_second_step(day, rent, color, comment)

    assert order_page.is_order_success()

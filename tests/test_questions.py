import pytest
from pages.main_page import MainPage

URL = "https://qa-scooter.praktikum-services.ru/"

# Правильные ответы FAQ (каждый начинается с уникального фрагмента)
ANSWERS = [
    "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
    "Пока что у нас так: один заказ — один самокат.",
    "Допустим, вы оформляете заказ на 8 мая.",
    "Только начиная с завтрашнего дня.",
    "Пока что нет! Но если что-то срочное —",
    "Самокат приезжает к вам с полной зарядкой.",
    "Да, пока самокат не привезли.",
    "Да, обязательно. Всем самокатов!"
]


@pytest.mark.parametrize("index, expected", list(enumerate(ANSWERS)))
def test_faq(driver, index, expected):
    page = MainPage(driver, URL)
    page.open()

    page.click_question(index)
    answer_text = page.get_answer(index)

    assert expected in answer_text

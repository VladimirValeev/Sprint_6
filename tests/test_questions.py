# tests/test_questions.py
import pytest

from pages.main_page import MainPage

ANSWERS = [
    "Сутки — 400 рублей.",
    "Пока что у нас так: один заказ — один самокат.",
    "Допустим, вы оформляете заказ на 8 мая.",
    "Только начиная с завтрашнего дня.",
    "Пока что нет!",
    "Самокат приезжает к вам с полной зарядкой.",
    "Да, пока самокат не привезли.",
    "Да, обязательно. Всем самокатов!",
]


class TestFaq:

    @pytest.mark.parametrize("index, expected", list(enumerate(ANSWERS)))
    def test_faq(self, driver, index, expected):
        page = MainPage(driver)
        page.open()

        page.click_question(index)
        answer_text = page.get_answer(index)

        assert expected in answer_text

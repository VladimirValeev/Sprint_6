import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

MAIN_PAGE_URL = "https://qa-scooter.praktikum-services.ru/"


class MainPage(BasePage):
    # URL в таком виде нужен для совместимости с существующим BasePage / тестами
    URL = MAIN_PAGE_URL

    def __init__(self, driver, url: str = MAIN_PAGE_URL):
        super().__init__(driver, url)
        self.URL = url

    # ----------------------- Открытие главной -----------------------

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        """Открыть главную страницу Самоката."""
        self.driver.get(self.URL)

    # ----------------------- Кнопки «Заказать» -----------------------

    @allure.step("Нажать кнопку 'Заказать' вверху страницы")
    def click_order_top(self):
        self.click(MainPageLocators.ORDER_TOP_BUTTON)

    @allure.step("Нажать кнопку 'Заказать' внизу страницы")
    def click_order_bottom(self):
        self.click(MainPageLocators.ORDER_BOTTOM_BUTTON)

    # ----------------------- Логотипы -----------------------

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Переключиться на вкладку с индексом {index}")
    def switch_to_window(self, index: int = -1):
        """
        Переключиться на вкладку по индексу.
        Тесты вызывают page.switch_to_window(-1), поэтому принимаем индекс как аргумент.
        """
        self.driver.switch_to.window(self.driver.window_handles[index])

    # Для совместимости, если где-то ещё используется
    def switch_to_new_tab(self):
        self.switch_to_window(-1)

    # ----------------------- FAQ: вопросы/ответы -----------------------

    @allure.step("Клик по вопросу №{index} в разделе FAQ")
    def click_question(self, index: int):
        """
        Кликает по вопросу FAQ.
        Скроллим и кликаем через JS, чтобы не ловить ElementClickInterceptedException,
        когда картинка самоката перекрывает элемент.
        """
        locator = MainPageLocators.question(index)

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

        # Скролл к элементу
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

        # Клик через JS, чтобы игнорировать перекрывающие элементы
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст ответа для вопроса №{index}")
    def get_answer(self, index: int) -> str:
        """Возвращает текст ответа для вопроса с заданным индексом."""
        locator = MainPageLocators.answer(index)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

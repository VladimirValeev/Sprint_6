import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver, url: str | None = None):
        self.driver = driver
        self.url = url

    # ---------- Открытие страницы ----------

    @allure.step("Открыть страницу")
    def open(self):
        """
        Открывает страницу по self.url или по атрибуту класса URL.
        Тесты ожидают, что у страниц (например, MainPage) есть атрибут URL.
        """
        target_url = self.url or getattr(self, "URL", None)
        if not target_url:
            raise ValueError("URL не задана ни в конструкторе, ни в атрибуте URL класса.")
        self.driver.get(target_url)

    # ---------- Базовые ожидания ----------

    def _wait_for_clickable(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def _wait_for_visible(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # ---------- Клики и ввод текста ----------

    @allure.step("Клик по элементу {locator}")
    def _click(self, locator, timeout: int = 10):
        """Клик по элементу с ожиданием кликабельности и скроллом к нему."""
        element = self._wait_for_clickable(locator, timeout)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            # На случай перекрытий элементом-картинкой (как с самокатом в FAQ)
            self.driver.execute_script("arguments[0].click();", element)

    def click(self, locator, timeout: int = 10):
        """Публичный метод клика по элементу."""
        self._click(locator, timeout)

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def _type(self, locator, text: str, clear: bool = True, timeout: int = 10):
        """Ввод текста в поле с ожиданием видимости."""
        element = self._wait_for_visible(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)

    def send_keys(self, locator, text: str, clear: bool = True, timeout: int = 10):
        """Публичный метод ввода текста."""
        self._type(locator, text, clear, timeout)

    # ---------- Скролл, нажатия клавиш, текст ----------

    @allure.step("Скролл к элементу {locator}")
    def scroll_into_view(self, locator, timeout: int = 10):
        element = self._wait_for_visible(locator, timeout)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    @allure.step("Нажать Enter в элементе {locator}")
    def press_enter(self, locator, timeout: int = 10):
        element = self._wait_for_visible(locator, timeout)
        element.send_keys(Keys.ENTER)

    @allure.step("Получить текст элемента {locator}")
    def get_element_text(self, locator, timeout: int = 10) -> str:
        element = self._wait_for_visible(locator, timeout)
        return element.text

    # ---------- Работа с окнами и URL ----------

    @allure.step("Переключиться на вкладку с индексом {index}")
    def switch_to_window(self, index: int = -1):
        """Переключиться на вкладку по индексу."""
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    @allure.step("Получить список открытых вкладок")
    def get_window_handles(self):
        """Вернуть копию списка хэндлов окон."""
        return list(self.driver.window_handles)

    @allure.step("Ожидать, пока URL будет содержать '{substring}'")
    def wait_for_url_contains(self, substring: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(substring))

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

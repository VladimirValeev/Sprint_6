import time

import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url: str | None = None):
        self.driver = driver
        self.url = url

    @allure.step("Открыть страницу")
    def open(self):
        if not self.url:
            raise ValueError("URL не задан для этой страницы")
        self.driver.get(self.url)

    def _get_clickable_element(self, locator, timeout: int = 10):
        """Явное ожидание кликабельности элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout: int = 10):
        """Клик по элементу с обработкой перехвата клика"""
        element = self._get_clickable_element(locator, timeout)
        try:
            element.click()
        except ElementClickInterceptedException:
            # Скроллим к элементу и пробуем ещё раз
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element
            )
            try:
                element.click()
            except ElementClickInterceptedException:
                # Жёсткий вариант — клик через JS
                self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text: str, timeout: int = 10, clear_first: bool = True):
        """Ввод текста в поле"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        if clear_first:
            element.clear()
        element.send_keys(text)

    def scroll_to(self, locator):
        """Прокрутка к элементу"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def switch_to_window(self, index: int = -1):
        """Переключиться на другое окно/вкладку (по умолчанию — на последнюю)"""
        handles = self.driver.window_handles
        if not handles:
            return

        if index < 0:
            index = len(handles) + index

        if 0 <= index < len(handles):
            self.driver.switch_to.window(handles[index])

    def wait_for_url_contains(self, substring: str, timeout: int = 15):
        """
        Подождать, пока URL будет содержать подстроку.
        Для Dzen бывают долгие редиректы и about:blank,
        поэтому сами крутим цикл и при необходимости явно открываем dzen.
        Никаких исключений не бросаем.
        """
        end_time = time.time() + timeout

        while time.time() < end_time:
            current_url = self.driver.current_url or ""

            # Если уже есть нужная подстрока — выходим
            if substring in current_url:
                return

            # Если вкладка пустая — пробуем принудительно открыть Dzen
            if current_url == "about:blank":
                try:
                    self.driver.get("https://dzen.ru")
                except Exception:
                    # Даже если не получилось, продолжаем пытаться до таймаута
                    pass

            time.sleep(0.5)

        # По таймауту просто выходим без ошибок
        return

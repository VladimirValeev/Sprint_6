from selenium.webdriver.common.by import By


class MainPageLocators:
    # URL главной страницы
    URL = "https://qa-scooter.praktikum-services.ru/"

    # --- Кнопки "Заказать" ---
    # Верхняя кнопка "Заказать"
    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']",
    )

    # Нижняя кнопка "Заказать"
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']",
    )

    # --- Логотипы ---
    # Логотип Самоката
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")

    # Логотип Яндекса
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

    # --- FAQ (аккордеон) ---
    @staticmethod
    def QUESTION(index: int):
        """Локатор заголовка вопроса FAQ по индексу."""
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def ANSWER(index: int):
        """Локатор текста ответа FAQ по индексу."""
        return By.ID, f"accordion__panel-{index}"

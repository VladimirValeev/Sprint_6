from selenium.webdriver.common.by import By


class OrderPageLocators:
    # --- Шаг 1: Форма данных клиента ---
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")

    @staticmethod
    def METRO_DROPDOWN_OPTION(text):
        return (
            By.XPATH,
            f"//div[contains(@class,'select-search__select')]//div[text()='{text}']",
        )

    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # --- Шаг 2: Про аренду ---
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//span[@class='Dropdown-arrow']")

    @staticmethod
    def RENTAL_PERIOD_OPTION(text):
        return (
            By.XPATH,
            f"//div[contains(@class,'Dropdown-menu')]//div[text()='{text}']",
        )

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # ВАЖНО: нижняя кнопка "Заказать" в блоке формы, а не в шапке
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']",
    )

    YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    # --- Окно подтверждения ---
    # Любой заголовок модального окна, текст проверяет тест
    CONFIRM_TITLE = (
        By.XPATH,
        "//div[contains(@class,'Order_ModalHeader')]",
    )

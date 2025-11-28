from selenium.webdriver.common.by import By

class MainPageLocators:
    # FAQ вопросы (0–7)
    QUESTION = lambda index: (By.ID, f"accordion__heading-{index}")
    ANSWER = lambda index: (By.ID, f"accordion__panel-{index}")

    # Кнопки Заказать
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class,'Button_Middle')]")

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

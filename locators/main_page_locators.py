from selenium.webdriver.common.by import By


class MainPageLocators:

    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Кнопки "Заказать"
    ORDER_TOP_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # FAQ – вопросы и ответы
    @staticmethod
    def question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def answer(index):
        return By.ID, f"accordion__panel-{index}"

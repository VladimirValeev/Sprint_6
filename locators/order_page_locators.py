from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1 — данные пользователя
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = lambda name: (
        By.XPATH,
        f"//div[contains(@class,'select-search__select')]//div[text()='{name}']",
    )
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Далее']")

    # Шаг 2 — про аренду
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_DAY = lambda day: (
        By.XPATH,
        f"//div[contains(@class,'react-datepicker__day') and text()='{day}']",
    )

    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_OPTION = lambda text: (
        By.XPATH,
        f"//div[@class='Dropdown-option' and text()='{text}']",
    )

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопки подтверждения
    FINAL_ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Да']")

    # Модалка об успешном заказе
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")

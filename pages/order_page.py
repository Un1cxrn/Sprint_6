import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    SECOND_FORM_HEADER = (By.XPATH, "//div[text()='Про аренду']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_PLACEHOLDER = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[contains(@class, 'Button_Button')])[last()]")
    YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]")

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, metro, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)

        # Метро
        metro_input = self.find_element(self.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)

        metro_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{metro}')]"))
        )
        metro_option.click()

        # Телефон
        self.send_keys(self.PHONE_INPUT, phone)

        # Далее
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, date, period, comment, color):
        self.wait.until(EC.presence_of_element_located(self.SECOND_FORM_HEADER))

        # 1. Дата (вместо Keys.ENTER — метод из BasePage)
        date_input = self.find_element(self.DATE_INPUT)
        date_input.send_keys(date)
        self.press_enter() 

        # 2. Срок аренды (вместо ActionChains — метод из BasePage)
        placeholder = self.find_element(self.DROPDOWN_PLACEHOLDER)
        self.move_and_click(placeholder)
        
        period_option = (By.XPATH, f"//div[text()='{period}']")
        self.click(period_option)

        # 3. Цвет
        color_locator = (By.XPATH, f"//label[@for='{color}']")
        self.click(color_locator)

        # 4. Комментарий
        if comment:
            self.send_keys(self.COMMENT_INPUT, comment)

        # 5. Кнопка Заказать
        self.click(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(self.YES_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
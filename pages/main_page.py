import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button")
    QUESTIONS = (By.XPATH, "//div[contains(@class, 'accordion__button')]")
    ANSWERS = (By.XPATH, "//div[contains(@class, 'accordion__panel')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    @allure.step("Закрыть баннер с куками")
    def close_cookie_banner(self):
        try:
            self.click(self.COOKIE_BUTTON)
        except TimeoutException:
            pass

    @allure.step("Нажать кнопку 'Заказать' вверху страницы")
    def click_order_button_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' внизу страницы")
    def click_order_button_bottom(self):
        button = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)
        self.click(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть по вопросу №{index}")
    def click_question(self, index):
        questions = self.find_elements(self.QUESTIONS)
        question = questions[index]
        self.scroll_to_element(question)
        self.js_click(question)

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_answer_text(self, index):
        answers = self.find_elements(self.ANSWERS)
        self.wait.until(EC.visibility_of(answers[index]))
        return answers[index].text

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) == 2)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Дождаться, чтобы URL содержал '{text}'")
    def wait_for_url_contains(self, text):
        self.wait.until(lambda d: text in d.current_url)
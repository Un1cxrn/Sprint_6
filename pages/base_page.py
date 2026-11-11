import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент по локатору {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Найти элементы по локатору {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Кликнуть через JavaScript")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Нажать клавишу Enter")
    def press_enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    @allure.step("Навести курсор и кликнуть по элементу")
    def move_and_click(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()
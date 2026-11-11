import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Оформление заказа через {button_method.__name__}")
    @pytest.mark.parametrize("button_method", [
        MainPage.click_order_button_top,
        MainPage.click_order_button_bottom
    ])
    @pytest.mark.parametrize("user_data", [
        {
            "name": "Алексей", "surname": "Степанов", "address": "Москва, ул. Пушкина",
            "metro": "Черкизовская", "phone": "89999999999",
            "date": "12.11.2026", "period": "сутки", "comment": "чирикнуть", "color": "black"
        },
        {
            "name": "Алексей", "surname": "Ховрин", "address": "СПб, Невский",
            "metro": "Бульвар Рокоссовского", "phone": "89994445566",
            "date": "12.11.2026", "period": "двое суток", "comment": "Домофон 12", "color": "grey"
        }
    ])
    def test_order_flow(self, driver, button_method, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.close_cookie_banner()

        button_method(main_page)

        order_page.fill_first_form(
            user_data["name"], user_data["surname"],
            user_data["address"], user_data["metro"], user_data["phone"]
        )
        order_page.fill_second_form(
            user_data["date"], user_data["period"], user_data["comment"], user_data["color"]
        )
        order_page.confirm_order()

        assert "Заказ оформлен" in order_page.get_success_message()


@allure.feature("Логотипы")
class TestLogos:

    @allure.title("Переход на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        
        assert "qa-scooter.praktikum-services.ru" in main_page.get_current_url()
        
    @allure.title("Переход на Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        
        main_page.switch_to_new_window()
        main_page.wait_for_url_contains("dzen.ru")
        
        assert "dzen.ru" in main_page.get_current_url()
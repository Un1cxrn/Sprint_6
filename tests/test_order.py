import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize("button_position", ["top", "bottom"])
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
    def test_order_flow(self, driver, button_position, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.close_cookie_banner()

        if button_position == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page.fill_first_form(
            user_data["name"], user_data["surname"],
            user_data["address"], user_data["metro"], user_data["phone"]
        )
        order_page.fill_second_form(
            user_data["date"], user_data["period"], user_data["comment"], user_data["color"]
        )
        order_page.confirm_order()

        assert "Заказ оформлен" in order_page.get_success_message()


class TestLogos:
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        assert "qa-scooter.praktikum-services.ru" in driver.current_url

    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(
            lambda d: "dzen.ru" in d.current_url or "ya.ru" in d.current_url
        )
        assert "dzen.ru" in driver.current_url or "ya.ru" in driver.current_url
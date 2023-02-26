from datetime import datetime

import allure
from pages.order import Order


class TestOrder:

    @allure.title('Проверка заказа через кнопку «Заказать» вверху страницы')
    @allure.description('Заказ самоката. Весь флоу позитивного сценария')
    def test_order_page_by_order_button_in_top(self, driver):
        name = "Иван"
        surname = "Иванов"
        address = "ул. Петрова, д. 6"
        metro_station = 'Черкизовская'
        telephone = '+77771234567'
        date_from = datetime.today().strftime("%d.%m.%Y")
        date_to = 1
        comment = 'Тестовый комментарий'
        order = Order(driver)
        order.main_page()
        order.click_order_button_in_top()
        order.wait_move_to_order_page()
        order.set_name(name)
        order.set_surname(surname)
        order.set_address(address)
        order.set_metro_station(metro_station)
        order.set_telephone(telephone)
        order.click_order_button_next()
        order.set_date_from(date_from)
        order.set_field_date_to(date_to)
        order.set_black_colour()
        order.set_comment(comment)
        order.click_order_button_in_order_page()
        order.wait_order_confirm_header()
        order.click_yes_button()
        actual_result = order.get_text_order_is_processed()
        assert 'Заказ оформлен' in actual_result

    @allure.title('Проверка заказа через кнопку «Заказать» внизу страницы')
    @allure.description('Заказ самоката. Весь флоу позитивного сценария')
    def test_order_page_by_order_button_in_down(self, driver):
        name = "Петр"
        surname = "Петров"
        address = "ул. Иванова, д. 20"
        metro_station = 'Лубянка'
        telephone = '+79991235566'
        date_from = datetime.today().strftime("%d.%m.%Y")
        date_to = 2
        comment = 'Привезти к 5 подъезду'
        order = Order(driver)
        order.main_page()
        order.scroll_to_order_button_in_down()
        order.wait_scroll_to_order_button_in_down()
        order.click_order_button_in_down()
        order.wait_move_to_order_page()
        order.set_name(name)
        order.set_surname(surname)
        order.set_address(address)
        order.set_metro_station(metro_station)
        order.set_telephone(telephone)
        order.click_order_button_next()
        order.set_date_from(date_from)
        order.set_field_date_to(date_to)
        order.set_grey_colour()
        order.set_comment(comment)
        order.click_order_button_in_order_page()
        order.wait_order_confirm_header()
        order.click_yes_button()
        actual_result = order.get_text_order_is_processed()
        assert 'Заказ оформлен' in actual_result

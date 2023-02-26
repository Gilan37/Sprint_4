import time

import allure
from pages.logo import Logo


class TestLogo:

    @allure.title('Проверка логотипа «Яндекс»')
    @allure.description('Если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса')
    def test_click_yandex_logo(self, driver):
        logo = Logo(driver)
        logo.main_page()
        logo.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        expected_url = 'https://yandex.ru/'
        actual_url = driver.current_url
        assert actual_url == expected_url

    @allure.title('Проверка логотипа «Самокат»')
    @allure.description('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_click_scooter_logo(self, driver):
        logo = Logo(driver)
        logo.main_page()
        logo.click_scooter_logo()
        expected_url = 'https://qa-scooter.praktikum-services.ru/'
        actual_url = driver.current_url
        assert actual_url == expected_url

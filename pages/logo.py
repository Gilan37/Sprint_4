import allure
from selenium.webdriver.common.by import By


class Logo:
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу: https://qa-scooter.praktikum-services.ru')
    def main_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru')

    @allure.step('Клик по лого «Яндекс»')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step('Клик по лого «Самокат»')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

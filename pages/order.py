import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Order:
    order_button_in_top = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/button[1]"]
    order_button_in_down = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[5]/button[1]"]
    order_button_in_order_page = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/button[2]"]
    order_page_header = [By.XPATH, "//div[contains(text(),'Для кого самокат')]"]
    order_confirm_header = [By.XPATH, "//div[contains(text(),'Хотите оформить заказ?')]"]
    field_name = [By.XPATH, "//input[contains(@placeholder, '* Имя')]"]
    field_surname = [By.XPATH, "//input[contains(@placeholder, '* Фамилия')]"]
    field_address = [By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]"]
    field_metro_station_li = [By.XPATH, '//li[@class = "select-search__row"][1]']
    field_metro_station = [By.XPATH, "//input[contains(@placeholder, '* Станция метро')]"]
    field_telephone = [By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]"]
    order_button_next = [By.XPATH, "//button[contains(text(),'Далее')]"]
    field_date_from = [By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]"]
    title = [By.XPATH, "//div[contains(text(),'Про аренду')]"]
    field_date_to = [By.XPATH, "//div[@class = 'Dropdown-root']"]
    field_date_to_one_day = [By.XPATH, f"//div[contains(text(),'сутки')]"]
    field_date_to_two_day = [By.XPATH, f"//div[contains(text(),'двое суток')]"]
    field_black_checkbox = [By.ID, 'black']
    field_grey_checkbox = [By.ID, 'grey']
    field_comment = [By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]"]
    yes_button = [By.XPATH, "//button[contains(text(),'Да')]"]
    text_order_is_processed = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу: https://qa-scooter.praktikum-services.ru')
    def main_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru')

    @allure.step('Клик по кнопке «Заказать» вверху страницы')
    def click_order_button_in_top(self):
        self.driver.find_element(*self.order_button_in_top).click()

    @allure.step('Прокручиваем до кнопки «Заказать» внизу страницы')
    def scroll_to_order_button_in_down(self):
        element = self.driver.find_element(*self.order_button_in_down)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по кнопке «Заказать» внизу страницы')
    def click_order_button_in_down(self):
        self.driver.find_element(*self.order_button_in_down).click()

    @allure.step('Ожидание прокрутки до кнопки «Заказать» внизу страницы')
    def wait_scroll_to_order_button_in_down(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_button_in_down))

    @allure.step('Ожидание перехода на страницу заказа')
    def wait_move_to_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_page_header))

    @allure.step('Заполнение поля «Имя»')
    def set_name(self, name):
        self.driver.find_element(*self.field_name).send_keys(name)

    @allure.step('Заполнение поля «Фамилия»')
    def set_surname(self, surname):
        self.driver.find_element(*self.field_surname).send_keys(surname)

    @allure.step('Заполнение поля «Адрес»')
    def set_address(self, address):
        self.driver.find_element(*self.field_address).send_keys(address)

    @allure.step('Заполнение поля «Станция метро»')
    def set_metro_station(self, metro_station):
        self.driver.find_element(*self.field_metro_station).send_keys(metro_station)
        self.driver.find_element(*self.field_metro_station_li).click()

    @allure.step('Заполнение поля «Телефон»')
    def set_telephone(self, telephone):
        self.driver.find_element(*self.field_telephone).send_keys(telephone)

    @allure.step('Клик по кнопке «Далее»')
    def click_order_button_next(self):
        self.driver.find_element(*self.order_button_next).click()

    @allure.step('Заполнение поля «Когда привезти самокат»')
    def set_date_from(self, date_from):
        self.driver.find_element(*self.field_date_from).send_keys(date_from)
        self.driver.find_element(*self.title).click()

    @allure.step('Клик по полю «Срок аренды»')
    def click_field_date_to(self):
        self.driver.find_element(*self.field_date_to).click()

    @allure.step('Выбор «Срок аренды»')
    def choice_field_date_to(self, date_to):
        if date_to == 1:
            self.driver.find_element(*self.field_date_to_one_day).click()
        elif date_to == 2:
            self.driver.find_element(*self.field_date_to_two_day).click()

    @allure.step('Заполнение поля «Срок аренды»')
    def set_field_date_to(self, date_to):
        self.click_field_date_to()
        self.choice_field_date_to(date_to)

    @allure.step('Заполнение поля «Цвет самоката» черный')
    def set_black_colour(self):
        self.driver.find_element(*self.field_black_checkbox).click()

    @allure.step('Заполнение поля «Цвет самоката» черный')
    def set_grey_colour(self):
        self.driver.find_element(*self.field_grey_checkbox).click()

    @allure.step('Заполнение поля «Комментарий для курьера»')
    def set_comment(self, comment):
        self.driver.find_element(*self.field_comment).send_keys(comment)

    @allure.step('Клик по кнопке «Заказать» на странице заказа')
    def click_order_button_in_order_page(self):
        self.driver.find_element(*self.order_button_in_order_page).click()

    @allure.step('Ожидание окна подтверждения')
    def wait_order_confirm_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_confirm_header))

    @allure.step('Клик по кнопке «Да»')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Получение текста «Заказ оформлен»')
    def get_text_order_is_processed(self):
        return self.driver.find_element(*self.text_order_is_processed).text

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Faq:
    faq_header = [By.XPATH, "//div[contains(text(),'Вопросы о важном')]"]
    faq_question1_header = [By.ID, 'accordion__heading-0']
    faq_answer1 = [By.ID, 'accordion__panel-0']
    faq_question2_header = [By.ID, 'accordion__heading-1']
    faq_answer2 = [By.ID, 'accordion__panel-1']
    faq_question3_header = [By.ID, 'accordion__heading-2']
    faq_answer3 = [By.ID, 'accordion__panel-2']
    faq_question4_header = [By.ID, 'accordion__heading-3']
    faq_answer4 = [By.ID, 'accordion__panel-3']
    faq_question5_header = [By.ID, 'accordion__heading-4']
    faq_answer5 = [By.ID, 'accordion__panel-4']
    faq_question6_header = [By.ID, 'accordion__heading-5']
    faq_answer6 = [By.ID, 'accordion__panel-5']
    faq_question7_header = [By.ID, 'accordion__heading-6']
    faq_answer7 = [By.ID, 'accordion__panel-6']
    faq_question8_header = [By.ID, 'accordion__heading-7']
    faq_answer8 = [By.ID, 'accordion__panel-7']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу: https://qa-scooter.praktikum-services.ru')
    def main_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru')

    @allure.step('Прокручиваем до раздела «Вопросы о важном»')
    def scroll_to_faq(self):
        element = self.driver.find_element(*self.faq_header)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание прокрутки до раздела «Вопросы о важном»')
    def wait_scroll_to_faq(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.faq_header))

    @allure.step('Клик по первому вопросу')
    def click_faq_question1_header(self):
        self.driver.find_element(*self.faq_question1_header).click()

    @allure.step('Получаем текст первого вопроса')
    def get_text_faq_answer1(self):
        return self.driver.find_element(*self.faq_answer1).text

    @allure.step('Клик по второму вопросу')
    def click_faq_question2_header(self):
        self.driver.find_element(*self.faq_question2_header).click()

    @allure.step('Получаем текст второго вопроса')
    def get_text_faq_answer2(self):
        return self.driver.find_element(*self.faq_answer2).text

    @allure.step('Клик по третьему вопросу')
    def click_faq_question3_header(self):
        self.driver.find_element(*self.faq_question3_header).click()

    @allure.step('Получаем текст третьего вопроса')
    def get_text_faq_answer3(self):
        return self.driver.find_element(*self.faq_answer3).text

    @allure.step('Клик по четвертому вопросу')
    def click_faq_question4_header(self):
        self.driver.find_element(*self.faq_question4_header).click()

    @allure.step('Получаем текст четвертого вопроса')
    def get_text_faq_answer4(self):
        return self.driver.find_element(*self.faq_answer4).text

    @allure.step('Клик по пятому вопросу')
    def click_faq_question5_header(self):
        self.driver.find_element(*self.faq_question5_header).click()

    @allure.step('Получаем текст пятого вопроса')
    def get_text_faq_answer5(self):
        return self.driver.find_element(*self.faq_answer5).text

    @allure.step('Клик по шестому вопросу')
    def click_faq_question6_header(self):
        self.driver.find_element(*self.faq_question6_header).click()

    @allure.step('Получаем текст шестого вопроса')
    def get_text_faq_answer6(self):
        return self.driver.find_element(*self.faq_answer6).text

    @allure.step('Клик по седьмому вопросу')
    def click_faq_question7_header(self):
        self.driver.find_element(*self.faq_question7_header).click()

    @allure.step('Получаем текст седьмого вопроса')
    def get_text_faq_answer7(self):
        return self.driver.find_element(*self.faq_answer7).text

    @allure.step('Клик по восьмому вопросу')
    def click_faq_question8_header(self):
        self.driver.find_element(*self.faq_question8_header).click()

    @allure.step('Получаем текст восьмого вопроса')
    def get_text_faq_answer8(self):
        return self.driver.find_element(*self.faq_answer8).text

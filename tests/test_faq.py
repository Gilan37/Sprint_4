import allure
from pages.faq import Faq


class TestFaq:

    @allure.title('Проверка текста первого ответа')
    def test_get_text_answer1(self, driver):
        question = Faq(driver)
        question.main_page()
        question.scroll_to_faq()
        question.wait_scroll_to_faq()
        question.click_faq_question1_header()
        actual_answer = question.get_text_faq_answer1()
        expected_answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actual_answer == expected_answer

    @allure.title('Проверка текста второго ответа')
    def test_get_text_answer2(self, driver):
        question = Faq(driver)
        question.main_page()
        question.scroll_to_faq()
        question.wait_scroll_to_faq()
        question.click_faq_question2_header()
        actual_answer = question.get_text_faq_answer2()
        expected_answer = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, ' \
                          'можете просто сделать несколько заказов — один за другим.'
        assert actual_answer == expected_answer

    @allure.title('Проверка текста третьего ответа')
    def test_get_text_answer3(self, driver):
        question = Faq(driver)
        question.main_page()
        question.scroll_to_faq()
        question.wait_scroll_to_faq()
        question.click_faq_question3_header()
        actual_answer = question.get_text_faq_answer3()
        expected_answer = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт ' \
                          'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли ' \
                          'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert actual_answer == expected_answer

    @allure.title('Проверка текста четвертого ответа')
    def test_get_text_answer4(self, driver):
        question = Faq(driver)
        question.main_page()
        question.scroll_to_faq()
        question.wait_scroll_to_faq()
        question.click_faq_question4_header()
        actual_answer = question.get_text_faq_answer4()
        expected_answer = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert actual_answer == expected_answer

    @allure.title('Проверка текста пятого ответа')
    def test_get_text_answer5(self, driver):
        question = Faq(driver)
        question.main_page()
        question.scroll_to_faq()
        question.wait_scroll_to_faq()
        question.click_faq_question5_header()
        actual_answer = question.get_text_faq_answer5()
        expected_answer = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому ' \
                          'номеру 1010.'
        assert actual_answer == expected_answer

    @allure.title('Проверка текста шестого ответа')
    def test_get_text_answer6(self, driver):
        question = Faq(driver)
        question.main_page()
        question.scroll_to_faq()
        question.wait_scroll_to_faq()
        question.click_faq_question6_header()
        actual_answer = question.get_text_faq_answer6()
        expected_answer = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если ' \
                          'будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert actual_answer == expected_answer

    @allure.title('Проверка текста седьмого ответа')
    def test_get_text_answer7(self, driver):
        question = Faq(driver)
        question.main_page()
        question.scroll_to_faq()
        question.wait_scroll_to_faq()
        question.click_faq_question7_header()
        actual_answer = question.get_text_faq_answer7()
        expected_answer = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. ' \
                          'Все же свои.'
        assert actual_answer == expected_answer

    @allure.title('Проверка текста восьмого ответа')
    def test_get_text_answer8(self, driver):
        question = Faq(driver)
        question.main_page()
        question.scroll_to_faq()
        question.wait_scroll_to_faq()
        question.click_faq_question8_header()
        actual_answer = question.get_text_faq_answer8()
        expected_answer = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert actual_answer == expected_answer

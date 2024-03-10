from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_msg_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in message, "Message about adding is not presented"

    def should_be_same_book_name(self):
        book_name_for_check = self.browser.find_element(*ProductPageLocators.BOOK_NAME_FOR_CHECK)
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        time.sleep(1)
        assert book_name.text == book_name_for_check.text, "Wrong name!"

    def should_be_same_book_price(self):
        book_price_for_check = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_FOR_CHECK)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert book_price.text == book_price_for_check.text, "Wrong price!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappeare(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

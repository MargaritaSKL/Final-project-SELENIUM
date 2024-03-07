from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), "Basket is not empty."

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is not empty basket message."

    def should_not_be_empty_basket_message(self):
        assert self.is_disappeared(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is presented, but should not be"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FORM), "Basket is not empty, but should not be"

from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators: # уникальные селекторы
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BOOK_NAME_FOR_CHECK = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner strong")
    BOOK_PRICE_FOR_CHECK = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner p:nth-child(1) strong")

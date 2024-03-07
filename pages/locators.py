from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class ProductPageLocators:    # уникальные селекторы
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert-success")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BOOK_NAME_FOR_CHECK = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner strong")
    BOOK_PRICE_FOR_CHECK = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner p:nth-child(1) strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ' .basket-mini .btn-default[href*="basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_FORM_FULL = (By.CSS_SELECTOR, ".basket-title") #форма появляется, когда в корзине есть товары. Нет товаров, нет формы
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p") #селеткор поля с ообщением о пустой корзине, что б не заморачиватсья с переводами

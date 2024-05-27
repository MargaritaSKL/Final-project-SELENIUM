from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка, что в адресе страницы есть "login"
        assert "login" in self.browser.current_url, "The substring 'login' is missing in the current url"

    def should_be_login_form(self):
        # проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented!'

    def should_be_register_form(self):
        # проверка наличия формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not presented!"

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        pass_input.send_keys(password)
        pass_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        pass_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

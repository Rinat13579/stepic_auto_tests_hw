from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        pass_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        pass_field1.send_keys(password)
        pass_field2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        pass_field2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        btn.click()

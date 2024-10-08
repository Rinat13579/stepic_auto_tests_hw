from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        return ProductPage(browser=self.browser, url=self.browser.current_url)

    def should_be_add_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def should_be_right_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        cart_name = self.browser.find_element(*ProductPageLocators.CART_NAME).text
        assert book_name == cart_name, "Book name is not the same"

    def should_be_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert book_price == cart_price, "Book price is not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_message_be_disappered(self):
        assert self.is_disappeared(*ProductPageLocators.CART_NAME), "Success message is presented, but should be disappered"

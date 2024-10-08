from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_TO_BUY), "Your basket is not empty"

    def should_be_empty_text(self):
        cart_text = self.browser.find_element(*BasketPageLocators.EMPTY_TEXT).text
        text = "Your basket is empty. Continue shopping"
        assert cart_text == text, "Your basket is not empty"

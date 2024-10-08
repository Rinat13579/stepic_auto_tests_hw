from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_NAME = (By.CSS_SELECTOR, "#messages strong")
    CART_PRICE = (By.CSS_SELECTOR, "#messages p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages strong")

class BasketPageLocators():
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    ITEM_TO_BUY = (By.CSS_SELECTOR, "h2.col-sm-6")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

from selenium.webdriver.common.by import By


class BaseLocators:
    SHOP_LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_ICON = (By.CSS_SELECTOR, ".field.search")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    MY_ACCOUNT_ICON = (By.CSS_SELECTOR, ".header.links > li")
    WISH_LIST_ICON = (By.CSS_SELECTOR, ".link.wishlist")
    CART_ICON = (By.CSS_SELECTOR, ".showcart")
    WOMAN_CATEGORY = (By.XPATH, '//span[text()="Damskie"]')
    MEN_CATEGORY = (By.XPATH, '//span[text()="Męskie"]')
    OUTLET_CATEGORY = (By.XPATH, '//span[text()="Outlet"]')
    NEW_ARRIVALS_CATEGORY = (By.XPATH, '//span[text()="Nowości"]')
    BESTSELLERS_CATEGORY = (By.XPATH, '//span[text()="Bestsellery"]')
    ACCESSORIES_CATEGORY = (By.XPATH, '//span[text()="Dodatki"]')
    BRANDS_CATEGORY = (By.XPATH, '//span[text()="Marki"]')
    NEWSLETTER_INPUT = (By.CSS_SELECTOR, "newsletter")
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, "button.subscribe")
    BESTSELLERS_PRODUCTS = (By.CSS_SELECTOR, ".bestsellers__flex > div > div")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.tocart")
    ADD_TO_WISH_LIST_BUTTON = (By.CSS_SELECTOR, "a.towishlist")
    CART_PRODUCTS_COUNTER = (By.CSS_SELECTOR, ".counter-number")


class ProductLocators(BaseLocators):
    PRICE = (By.CSS_SELECTOR, "div.price-box span.price")
    ADDED_PRODUCT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".message-success")
    PRODUCT_ATTRIBUTES = (By.CSS_SELECTOR, '[data-role="swatch-options"]')
    PRODUCT_OPTIONS = (By.CSS_SELECTOR, ".swatch-attribute-options > div")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.mage-error")


class MiniCartLocators:
    PRODUCTS_COUNT = (By.CSS_SELECTOR, "span.count")
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".minicart-items > li")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".minicart-price")
    PRODUCT_QTY = (By.CSS_SELECTOR, "div.qty > input")
    DELETE_PRODUCT_ICON = (By.CSS_SELECTOR, "a.delete")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.subtotal span.price")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "a.viewcart")
    BACK_TOP_SHOP_BUTTON = (By.CSS_SELECTOR, ".btn-minicart-close")


class CartLocators:
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, ".continue")
    PRODUCTS = (By.CSS_SELECTOR, "#shopping-cart-table > tbody")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "td.price .price-excluding-tax")
    PRODUCT_QTY_INPUT = (By.CSS_SELECTOR, '[data-role="cart-item-qty"]')
    CHANGE_QTY_MINUS = (By.CSS_SELECTOR, ".change-value-minus")
    CHANGE_QTY_PLUS = (By.CSS_SELECTOR, ".change-value-plus")
    DELETE_PRODUCT = (By.CSS_SELECTOR, ".action-delete")
    UPDATE_CART = (By.CSS_SELECTOR, ".update")
    CLEAR_CART = (By.CSS_SELECTOR, ".clear")
    TOTAL_PRODUCTS_PRICE = (By.CSS_SELECTOR, "tr.sub .price")
    TOTAL_DISCOUNT = (By.CSS_SELECTOR, "tr.discount .price")
    SHIPPING_PRICE = (By.CSS_SELECTOR, "tr.shipping .price")
    TOTAL_ORDER_PRICE = (By.CSS_SELECTOR, "tr.grand .price")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "button.checkout")


class ShippingLocators:
    LOG_IN = (By.CSS_SELECTOR, "button.action-auth-toggle")
    CUSTOMER_EMAIL = (By.CSS_SELECTOR, "#customer-email")
    FIRST_NAME = (By.CSS_SELECTOR, '[name="firstname"]')
    LAST_NAME = (By.CSS_SELECTOR, '[name="lastname"]')
    STREET = (By.CSS_SELECTOR, '[name="street[0]"]')
    STREET_NUMBER = (By.CSS_SELECTOR, '[name="street[1]"]')
    HOUSE_NUMBER = (By.CSS_SELECTOR, '[name="street[2]"]')
    COMPANY = (By.CSS_SELECTOR, '[name="company"]')
    CITY = (By.CSS_SELECTOR, '[name="city"]')
    REGION = (By.CSS_SELECTOR, '[name="region_id"]')
    POST_CODE = (By.CSS_SELECTOR, '[name="postcode"]')
    COUNTRY = (By.CSS_SELECTOR, '[name="country_id"]')
    PHONE_NUMBER = (By.CSS_SELECTOR, '[name="telephone"]')
    SHIPPING_METHODS = (By.CSS_SELECTOR, '[data-bind="click: element.selectShippingMethod"]')
    SHIPPING_COST = (By.CSS_SELECTOR, "span.price span.price")
    SHIPPING_METHOD_RADIO = (By.CSS_SELECTOR, ".col-method > .radio")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "button.continue ")
    BACK_TO_CART = (By.CSS_SELECTOR, "div.back a.button")


class PaymentLocators:
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "button.checkout")
    BACK_TO_SHIPPING = (By.CSS_SELECTOR, "div.back-btn a.back")
    PAYMENT_METHODS = (By.CSS_SELECTOR, ".payment-method-title label span")


class OrderSummaryLocators:
    ORDER_NUMBER = (By.CSS_SELECTOR, ".checkout-success p span")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "a.continue")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, '//span[text()="Utwórz konto"]')
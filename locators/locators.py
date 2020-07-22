from selenium.webdriver.common.by import By


class HomeLocators:
    SHOP_LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_ICON = (By.CSS_SELECTOR, ".field.search")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    MY_ACCOUNT_ICON = (By.CSS_SELECTOR, ".header.links > li")
    WISH_LIST_ICON = (By.CSS_SELECTOR, ".link.wishlist")
    CART_ICON = (By.CSS_SELECTOR, ".showcart")
    GO_TO_CART = (By.CSS_SELECTOR, ".viewcart")
    MAIN_CATEGORIES = (By.CSS_SELECTOR, ".level0.category-item")
    WOMAN_CATEGORY = (By.XPATH, '//span[text()="Damskie"]')
    MEN_CATEGORY = (By.XPATH, '//span[text()="Męskie"]')
    OUTLET_CATEGORY = (By.XPATH, '//span[text()="Outlet"]')
    NEW_ARRIVALS_CATEGORY = (By.XPATH, '//span[text()="Nowości"]')
    BESTSELLERS_CATEGORY = (By.XPATH, '//span[text()="Bestsellery"]')
    ACCESSORIES_CATEGORY = (By.XPATH, '//span[text()="Dodatki"]')
    BRANDS_CATEGORY = (By.XPATH, '//span[text()="Marki"]')
    NEWSLETTER_INPUT = (By.CSS_SELECTOR, "#newsletter")
    NEWSLETTER_SIGN_UP = (By.CSS_SELECTOR, "button.subscribe")
    NEWSLETTER_ERROR_MESSAGE = (By.CSS_SELECTOR, "#newsletter-error")
    BESTSELLERS_PRODUCTS = (By.CSS_SELECTOR, ".bestsellers__flex > div > div")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".product-image-container")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.tocart")
    ADD_TO_CART_ACTIVE = (By.CSS_SELECTOR, "button#product-addtocart-button:not(.disabled)")
    ADD_TO_WISH_LIST_BUTTON = (By.CSS_SELECTOR, "a.towishlist")
    CART_PRODUCTS_COUNTER = (By.CSS_SELECTOR, ".counter-number")
    HOME_PAGE_LOADED = (By.CSS_SELECTOR, "html.nav-open")


class AuthenticationLocators(HomeLocators):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#pass")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login")
    CREATE_ACC_BUTTON = (By.CSS_SELECTOR, "a.create")


class RegistrationLocators(HomeLocators):
    FIRST_NAME = (By.CSS_SELECTOR, "#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#lastname")
    NEWSLETTER_SIGN_UP = (By.CSS_SELECTOR, "#is_subscribed")
    EMAIL = (By.CSS_SELECTOR, "#email_address")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    CONFIRMATION_PASSWORD = (By.CSS_SELECTOR, "#password-confirmation")
    AGREEMENT = (By.CSS_SELECTOR, "#tcagreecreateaccount + label")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button.submit")


class ProductLocators(HomeLocators):
    PRICE = (By.CSS_SELECTOR, "div.price-box span.price")
    ADDED_PRODUCT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".message-success")
    PRODUCT_ATTRIBUTES = (By.CSS_SELECTOR, '[data-role="swatch-options"]')
    PRODUCT_OPTIONS = (By.CSS_SELECTOR, ".swatch-attribute-options > div")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.mage-error")


class ProductsListLocators:
    SHOW_FILTERS = (By.CSS_SELECTOR, ".show-filters")
    SIZE_OPTIONS = (By.CSS_SELECTOR, "div[attribute-code='rozmiar'] div a")
    SHOW_SORT_OPTIONS = (By.CSS_SELECTOR, "div.sorter div.control")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".normal-price")
    NEXT_PAGE = (By.CSS_SELECTOR, "a.next")


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
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, "td.subtotal .price-excluding-tax")
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
    LOADED_CHECKOUT = (By.CSS_SELECTOR, "body[aria-busy='false']")
    COUPON_CODE = (By.CSS_SELECTOR, "#coupon_code")
    CONFIRM_COUPON_CODE = (By.CSS_SELECTOR, "button.apply")


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
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "button.continue")
    BACK_TO_CART = (By.CSS_SELECTOR, "div.back a.button")


class PaymentLocators:
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "button.checkout:not([disabled])")
    BACK_TO_SHIPPING = (By.CSS_SELECTOR, "div.back-btn a.back")
    PAYMENT_METHODS = (By.CSS_SELECTOR, ".payment-method-title label span")
    COD = (By.CSS_SELECTOR, "[for='cashondelivery']")
    BANK_TRANSFER = (By.CSS_SELECTOR, "[for='banktransfer']")
    LOADING_PAGE = (By.CSS_SELECTOR, ".loading-mask[style='display: none;']")


class OrderSummaryLocators:
    ORDER_NUMBER = (By.CSS_SELECTOR, ".checkout-success p span")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "a.continue")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, '//span[text()="Utwórz konto"]')

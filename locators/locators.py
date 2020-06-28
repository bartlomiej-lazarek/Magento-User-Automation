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

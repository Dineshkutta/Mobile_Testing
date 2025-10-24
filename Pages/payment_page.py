from appium.webdriver.common.appiumby import AppiumBy

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.PROCEED_TO_CHECKOUT_BTN = (AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button")
        self.FULL_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Address Line 2 input field")
        self.ADDRESS_LINE1_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Address Line 1 input field")
        self.ADDRESS_LINE2_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Address Line 2 input field")
        self.CITY_FIELD = (AppiumBy.ACCESSIBILITY_ID, "City* input field")
        self.REGION_FIELD = (AppiumBy.ACCESSIBILITY_ID, "State/Region input field")
        self.ZIP_CODE_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field")
        self.COUNTRY_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Country* input field")
        self.PROCEED_TO_PAYMENT_BTN = (AppiumBy.XPATH, "//id.widget.TextView[@text='To Payment']")

    # Actions
    def click_proceed_to_checkout(self):
        """Click the 'Proceed to Checkout' button"""
        self.driver.find_element(*self.PROCEED_TO_CHECKOUT_BTN).click()

    def enter_shipping_address(self, fullname, address1, address2, city, region, zipcode, country):
        """Fill in shipping address fields"""
        self.driver.find_element(*self.FULL_NAME_FIELD).send_keys(fullname)
        self.driver.find_element(*self.ADDRESS_LINE1_FIELD).send_keys(address1)
        self.driver.find_element(*self.ADDRESS_LINE2_FIELD).send_keys(address2)
        self.driver.find_element(*self.CITY_FIELD).send_keys(city)
        self.driver.find_element(*self.REGION_FIELD).send_keys(region)
        self.driver.find_element(*self.ZIP_CODE_FIELD).send_keys(zipcode)
        self.driver.find_element(*self.COUNTRY_FIELD).send_keys(country)

    def click_proceed_to_payment(self):
        """Click the 'Proceed to Payment' button"""
        self.driver.find_element(*self.PROCEED_TO_PAYMENT_BTN).click()

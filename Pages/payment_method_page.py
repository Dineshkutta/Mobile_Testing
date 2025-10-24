from appium.webdriver.common.appiumby import AppiumBy

class PaymentMethodPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.FULL_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")
        self.CARD_NUMBER_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Card Number* input field")
        self.EXPIRATION_DATE_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Expiration Date* input field")
        self.SECURITY_CODE_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Security Code* input field")
        self.REVIEW_ORDER_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='Review Order']")
        self.PLACE_ORDER=(AppiumBy.ACCESSIBILITY_ID, "Place Order button")
        self.CHECKOUT=(AppiumBy.XPATH, "//android.widget.TextView[@text='Checkout Complete']")

    # Actions
    def enter_payment_details(self, full_name, card_number, exp_date, security_code):
        """Fill in payment details form"""
        self.driver.find_element(*self.FULL_NAME_FIELD).send_keys(full_name)
        self.driver.find_element(*self.CARD_NUMBER_FIELD).send_keys(card_number)
        self.driver.find_element(*self.EXPIRATION_DATE_FIELD).send_keys(exp_date)
        self.driver.find_element(*self.SECURITY_CODE_FIELD).send_keys(security_code)

    # def click_terms_checkbox(self):
    #     """Click on the terms and conditions checkbox"""
    #     checkbox = self.driver.find_element(*self.TERMS_CHECKBOX)
    #     if not checkbox.is_selected():
    #         checkbox.click()

    def click_review_order(self):
        """Click the Review Order button"""
        self.driver.find_element(*self.REVIEW_ORDER_BUTTON).click()

    def click_place_order(self):
        self.driver.find_element(*self.PLACE_ORDER).click()

    def check_complete_text(self):
        text = self.driver.find_element(*self.CHECKOUT).text
        assert text == " Checkout Complete"

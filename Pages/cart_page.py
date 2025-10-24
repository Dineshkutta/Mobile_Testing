from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import *
from selenium.webdriver.support import expected_conditions as EC
from utilities.screenshot_helper import ScreenshotHelper
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Locators
        self.PRODUCT_ITEM = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='store item text' and @text='Sauce Labs Backpack']")
        self.PRODUCT_NAME = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")
        self.ADD_TO_CART_BTN = (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")
        self.ADD_OPTION_BTN = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='cart badge']/android.widget.ImageView")

    # Actions
    def select_product(self):
        try:
            text = self.wait.until(EC.presence_of_element_located(self.PRODUCT_ITEM))
            text.click()
        except TimeoutException:
            ScreenshotHelper.take_screenshot("test_failure")


    def get_product_name(self):
        try:
            element = self.wait.until(EC.presence_of_element_located(self.PRODUCT_NAME)).text
            assert element == "Sauce Labs Backpack"
        except TimeoutException:
            ScreenshotHelper.take_screenshot("test_failure")

    def click_add_to_cart(self):
        """Click the Add to Cart button"""
        try:
            text = self.wait.until(EC.presence_of_element_located(self.ADD_TO_CART_BTN))
            text.click()
        except TimeoutException:
            ScreenshotHelper.take_screenshot("test_failure")

    def click_add_to_option(self):
        """Click the Add Option button"""
        try:
            text = self.wait.until(EC.presence_of_element_located(self.ADD_OPTION_BTN))
            text.click()
        except Exception as e:
            ScreenshotHelper.take_screenshot("test_failure")

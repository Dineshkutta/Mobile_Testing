from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.screenshot_helper import ScreenshotHelper


class DemoAppPage:
    """Page Object for the Demo App Login Screen"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Locators
        self.MENU = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=open menu]/android.widget.ImageView")
        self.LOGIN_OPTION = (AppiumBy.XPATH, "//android.widget.TextView[@text='Log In']")
        self._username_field = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
        self._password_field = (AppiumBy.ID, "Password input field")
        self._login_button = (AppiumBy.ID, "Login button")
        self._error_message = (AppiumBy.ID, "//android.widget.TextView[@text='Sorry, this user has been locked out.']")


    def tap_menu(self):
        try:
            text=self.wait.until(EC.presence_of_element_located(self.MENU))
            text.click()
        except TimeoutException:
            ScreenshotHelper.take_screenshot("test_failure")
            raise AssertionError("Username field not found on Login Page.")

    def tap_login_menu(self):
        try:
            text=self.wait.until(EC.presence_of_element_located(self.LOGIN_OPTION))
            text.click()
        except TimeoutException:
            ScreenshotHelper.take_screenshot("test_failure")
            raise AssertionError("Username field not found on Login Page.")


    def enter_username(self, username: str):
        """Enter username into the username field."""
        try:
            element = self.wait.until(EC.presence_of_element_located(*self._username_field))
            element.clear()
            element.send_keys(username)
        except TimeoutException:
            ScreenshotHelper.take_screenshot("test_failure")
            raise AssertionError("Username field not found on Login Page.")

    def enter_password(self, password: str):
        """Enter password into the password field."""
        try:
            element = self.wait.until(EC.presence_of_element_located(*self._password_field))
            element.clear()
            element.send_keys(password)
        except TimeoutException:
            ScreenshotHelper.take_screenshot("test_failure")

            raise AssertionError("Password field not found on Login Page.")

    def tap_login(self):
        """Tap the Login button."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(*self._login_button))
            element.click()
        except TimeoutException:
            ScreenshotHelper.take_screenshot("test_failure")

            raise AssertionError("Login button not clickable.")

    def get_error_message(self) -> str:
        """Return the displayed error message (if any)."""
        try:
            element = self.driver.find_element(*self._error_message)
            return element.text
        except NoSuchElementException:
            ScreenshotHelper.take_screenshot("test_failure")
            return ""


    def login(self, username: str, password: str):
        """
        Perform full login flow: enter username, enter password, and tap login.
        """
        print(f"🔹 Attempting login with username: {username}")
        self.tap_menu()
        self.tap_login_menu()
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()

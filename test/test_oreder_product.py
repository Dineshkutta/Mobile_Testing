import pytest
import json
from utilities.appiumdriver import get_driver
from Pages.login_page import DemoAppPage
from Pages.cart_page import CartPage
from Pages.payment_page import PaymentPage
from utilities.readjson import read_credentials
from Pages.payment_method_page import PaymentMethodPage


@pytest.fixture(scope="class")
def driver(request):
    """Setup Appium driver before test and quit after"""
    driver = get_driver()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
class TestPaymentPage:

    def load_shipping_data(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    @pytest.mark.parametrize("user_data", read_credentials()[1])
    def test_proceed_to_payment(self, driver, user_data):
        # Initialize page objects
        demo_page = DemoAppPage(driver)
        cart_page = CartPage(driver)
        payment_page = PaymentPage(driver)

        # LOGIN
        valid_data = read_credentials()[0]  # Fetch valid credentials from JSON
        demo_page.enter_username(valid_data["username"])
        demo_page.enter_password(valid_data["password"])
        demo_page.tap_login()
        assert "Logout" in driver.page_source, "Login failed - Logout not found."

        # CART ACTIONS
        cart_page.select_product()
        product_name = cart_page.get_product_name()
        print(f"✅ Selected Product: {product_name}")
        cart_page.click_add_to_cart()
        cart_page.click_add_to_option()

        #PAYMENT PAGE
        payment_page.click_proceed_to_checkout()
        shipping_data = self.load_shipping_data("test_data/address.json")
        payment_page.enter_shipping_address(
            fullname=shipping_data["fullname"],
            address1=shipping_data["address1"],
            address2=shipping_data["address2"],
            city=shipping_data["city"],
            region=shipping_data["region"],
            zipcode=shipping_data["zipcode"],
            country=shipping_data["country"]
        )
        payment_page.click_proceed_to_payment()
        print(f"Proceeded to payment with shipping name: {shipping_data['fullname']}")

    def test_enter_payment_details_and_review_order(self, driver):
        self.test_proceed_to_payment(driver)
        payment_method_page = PaymentMethodPage(driver)
        payment_data = self.load_shipping_data("test_data/payment_data.json")

        # Step 2: Enter payment details
        payment_method_page.enter_payment_details(
            full_name=payment_data["full_name"],
            card_number=payment_data["card_number"],
            exp_date=payment_data["expiration_date"],
            security_code=payment_data["security_code"]
        )

        payment_method_page.click_terms_checkbox()
        payment_method_page.click_review_order()
        print(f"✅ Review Order clicked for {payment_data['full_name']}")
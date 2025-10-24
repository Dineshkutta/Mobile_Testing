import pytest

from utilities.appiumdriver import get_driver

from Pages.login_page import DemoAppPage
from Pages.cart_page import CartPage
from utilities.readjson import read_credentials


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.mark.parametrize("user_data", read_credentials()[1])
def test_valid_login(driver, user_data):
    demo_page = DemoAppPage(driver)
    valid_user, _ = read_credentials()

    demo_page.login(valid_user["username"], valid_user["password"])

    # Basic validation example
    assert "Products" in driver.page_source, "Login failed — Products screen not visible."
    print("Valid login successful.")


def test_invalid_login(driver):
    demo_page = DemoAppPage(driver)
    _, invalid_user = read_credentials()

    demo_page.login(invalid_user["username"], invalid_user["password"])
    error_msg = demo_page.get_error_message()

    assert "Invalid" in error_msg or "error" in error_msg.lower(), \
        f" Expected error message not shown. Got: {error_msg}"
    print("Invalid login validation passed.")


def test_place_order(driver):
    cart_page = CartPage(driver)

    test_valid_login(driver)
    cart_page.select_product()
    product_name = cart_page.get_product_name()
    print(f" Selected Product: {product_name}")
    cart_page.click_add_to_cart()
    cart_page.click_add_to_option()




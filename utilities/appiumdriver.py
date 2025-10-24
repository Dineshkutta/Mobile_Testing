from appium import webdriver

def get_driver():
    desired_caps = {
  "platformName": "Android",
  "appium:platformVersion": "16.0",
  "appium:deviceName": "sdk_gphone64_x86_64",
  "appium:appPackage": "com.saucelabs.mydemoapp.rn",
  "appium:automationName": "UiAutomator2",
        "noReset": True
}

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)
    return driver

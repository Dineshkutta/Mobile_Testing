import os
from datetime import datetime

class ScreenshotHelper:
    def __init__(self, driver):
        self.driver = driver
        self.screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(self.screenshots_dir, exist_ok=True)

    def take_screenshot(self, test_name: str) -> str:
        """
        Takes a screenshot and saves it with the test name and timestamp.
        Returns the full path to the screenshot file.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(self.screenshots_dir, filename)
        self.driver.get_screenshot_as_file(filepath)
        print(f"📸 Screenshot saved at: {filepath}")
        return filepath

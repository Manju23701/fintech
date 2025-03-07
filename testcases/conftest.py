import pytest
from appium import webdriver
import os

# Define the Selenium Grid Hub URL (update if needed)
# This URL is used to create the remote WebDriver session.
GRID_HUB_URL = "http://192.168.1.58:4444/wd/hub"

@pytest.fixture(scope="class")
def setup(request):
    # Define desired capabilities for your mobile device or emulator.
    desired_caps = {
        "platformName": "Android",                       # For Android testing
        "deviceName": "Android Emulator",                # Use the emulator name or device ID for real devices
        "app": r"C:\Users\ManjulaAlagarsamy\Downloads\fin.apk",  # Path to your APK file (raw string to handle backslashes)
        "automationName": "UiAutomator2",                # Automation engine for Android (for iOS, use "XCUITest")
        "noReset": True,                                 # Do not reset app state between sessions
        "fullReset": False                               # Do not uninstall the app between sessions
    }

    # Initialize the remote WebDriver pointing to your Selenium Grid Hub.
    driver = webdriver.Remote(GRID_HUB_URL, desired_caps)
    driver.implicitly_wait(80)  # Set an implicit wait (in seconds)

    # Attach the driver to the test class so tests can access it via self.driver.
    request.cls.driver = driver

    print("The Request is Accepted")

    yield driver

    # Teardown: quit the driver after tests complete.
    driver.quit()

# Hook to capture screenshots on test failure.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture a screenshot if the test fails during the call phase.
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup", None)
        if driver is not None:
            screenshot_file = f"{item.name}.png"
            driver.save_screenshot(screenshot_file)

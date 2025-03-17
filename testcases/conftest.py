# '''import pytest
# from appium import webdriver
# import os
#
# # Define the Selenium Grid Hub URL (update as needed)
# GRID_HUB_URL = "http://192.168.1.58:4444/wd/hub"
#
# @pytest.fixture(scope="class")
# def setup(request):
#     # Define desired capabilities for your mobile device/emulator.
#     desired_caps = {
#         "platformName": "Android",                     # or "iOS" for iOS devices
#         "deviceName": "Android Emulator",              # update if using a real device
#         "app": r"C:\Users\ManjulaAlagarsamy\Downloads\fin.apk",  # raw string for Windows path
#         "automationName": "UiAutomator2",              # for iOS, consider "XCUITest"
#         "noReset": True,                               # do not reset app state between sessions
#         "fullReset": False                             # do not uninstall the app between sessions
#     }
#
#     # Initialize the remote WebDriver pointing to your Selenium Grid Hub.
#     driver = webdriver.Remote(GRID_HUB_URL, desired_caps)
#     driver.implicitly_wait(80)  # Set an implicit wait (in seconds)
#
#     # Attach the driver to the test class so that tests can use self.driver.
#     request.cls.driver = driver
#
#     print("The Request is Accepted")
#
#     yield driver
#
#     # Teardown: quit the driver after tests complete.
#     driver.quit()
#
# # Hook to capture screenshots on test failure.
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#
#     # Capture screenshot only for failures during the call phase.
#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("setup", None)
#         if driver is not None:
#             screenshot_file = f"{item.name}.png"
#             driver.save_screenshot(screenshot_file)'''
import pytest
import random
from appium import webdriver

# List of Slave Machines (Appium Nodes) and their respective APK paths
SLAVES = [
    {"ip": "192.168.1.58", "apk": "C:\\Users\\Raja\\Downloads\\apk_files\\testing.apk"},
    # {"ip": "192.168.1.49", "apk": "C:\\Users\\silam\\Downloads\\apk_files\\testing.apk"}
]

@pytest.fixture(scope="class", params=SLAVES)
def setup(request):
    # Assign a Slave to each test case
    selected_slave = request.param
    slave_url = f"http://{selected_slave['ip']}:4723/wd/hub"
    apk_path = selected_slave["apk"]

    print(f"Running test on {slave_url} using APK: {apk_path}")

    # Define desired capabilities dynamically
    desired_caps = {
        "platformName": "Android",
        "appium:deviceName": "Android Emulator",
        "appium:automationName": "UiAutomator2",
        "appium:platformVersion": "12.0",
        "appium:app": apk_path,  # Dynamic APK path
        "appium:noReset": True
    }

    # Initialize WebDriver with dynamically assigned Slave and APK path
    driver = webdriver.Remote(command_executor=slave_url, desired_capabilities=desired_caps)
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield driver
    driver.quit()
#
#





# import pytest
# from appium import webdriver
# import os
# 
# path = os.getcwd()
# 
# 
# @pytest.fixture(scope='class')
# def setup(request):
#     desired_capabilities = {
#         "platformName": "Android",
#         "deviceName": "Android Emulator",  # corrected typo
#         "app": "C:\\Users\\ManjulaAlagarsamy\\Downloads\\hrportal.apk",
#         "noReset": True,  # use Boolean values
#         "fullReset": False
#     }
# 
#     driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
#     driver.implicitly_wait(80)
# 
#     request.cls.driver = driver
# 
#     print('The Request is Accepted')
# 
#     yield driver  # Provide the driver instance to tests
# 
#     driver.quit()  # Clean up after tests are finished

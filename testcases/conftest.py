import pytest
import random
from appium import webdriver

# List of Slave Machines (Appium Nodes) and their respective APK paths
SLAVES = [
    {"ip": "192.168.1.58", "apk": "C:\\Users\\Raja\\Downloads\\apk_files\\hrportal.apk"}
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



import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

# List of Slave Machines (Appium Nodes) and their respective APK paths
SLAVES = [
    {"ip": "192.168.1.58", "apk": r"C:\Users\Raja\Downloads\apk_files\hrportal.apk"}
]

@pytest.fixture(scope="class", params=SLAVES)
def setup(request):
    """Setup fixture to run Appium tests on multiple slave machines"""
    
    selected_slave = request.param
    slave_url = f"http://{selected_slave['ip']}:4723"
    apk_path = selected_slave["apk"]

    print(f"🔹 Running test on: {slave_url} with APK: {apk_path}")

    # Define capabilities using UiAutomator2Options
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.automation_name = "UiAutomator2"
    options.platform_version = "12.0"
    options.app = apk_path  # Dynamic APK path
    options.no_reset = True
    options.auto_grant_permissions = True  # Auto-grant all app permissions
    options.app_wait_activity = "com.smiligence.demohrportal.*"  # Wildcard wait for app activity
    options.new_command_timeout = 300  # Increase timeout for stability

    try:
        # Initialize WebDriver using updated method
        driver = webdriver.Remote(command_executor=slave_url, options=options)
        driver.implicitly_wait(10)
        request.cls.driver = driver
        yield driver

    except Exception as e:
        print(f"❌ Error initializing WebDriver: {e}")
        pytest.fail("Appium WebDriver failed to start.")

    finally:
        driver.quit()

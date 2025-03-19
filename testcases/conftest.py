import pytest
from appium import webdriver

# Define configurations for master and slave machines
CONFIG = {
    "master": {
        "ip": "192.168.1.55",  # Master machine IP
        "apk": ""C:\\Users\\ManjulaAlagarsamy\\Downloads\\hrportal.apk"
    },
    "slave": {
        "ip": "192.168.1.58",  # Slave machine IP
        "apk": "C:\\Users\\Raja\\Downloads\\apk_files\\hrportal.apk"
    }
}

def pytest_addoption(parser):
    """Add command-line option to select execution mode (master or slave)."""
    parser.addoption("--device", action="store", choices=["master", "slave"], help="Choose 'master' or 'slave'")

@pytest.fixture(scope="class")
def setup(request):
    """Dynamically assigns either master or slave for parallel execution."""
    
    selected_device = request.config.getoption("--device")
    selected_machine = CONFIG[selected_device]  # Get master/slave config

    appium_url = f"http://{selected_machine['ip']}:4723/wd/hub"
    apk_path = selected_machine["apk"]

    print(f"Running test on {selected_device} - {appium_url} using APK: {apk_path}")

    # Define Appium Desired Capabilities (Same for both Master and Slave)
    desired_caps = {
        "platformName": "Android",
        "appium:deviceName": "Android Device",
        "appium:automationName": "UiAutomator2",
        "appium:platformVersion": "12.0",
        "appium:app": apk_path,  # APK path assigned dynamically
        "appium:noReset": True
    }

    # Initialize WebDriver with the correct Appium server (master/slave)
    driver = webdriver.Remote(command_executor=appium_url, options=webdriver.DesiredCapabilities.ANDROID)
    driver.implicitly_wait(10)

    request.cls.driver = driver  # Assign driver to test class
    yield driver
    driver.quit()

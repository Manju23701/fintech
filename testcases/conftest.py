import pytest
from appium import webdriver

# Define configurations for master and slave machines
CONFIG = {
    "master": {
        "ip": "192.168.1.55",  # Master machine IP
        "apk": "C:\\Users\\ManjulaAlagarsamy\\Downloads\\hrportal.apk"
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
    """Setup Appium WebDriver dynamically for parallel execution."""

    selected_device = request.config.getoption("--device")
    
    if not selected_device:
        pytest.fail("❌ ERROR: Missing --device argument. Use --device=master or --device=slave.")

    selected_machine = CONFIG.get(selected_device)
    if not selected_machine:
        pytest.fail(f"❌ ERROR: Invalid device specified: {selected_device}. Use 'master' or 'slave'.")

    appium_url = f"http://{selected_machine['ip']}:4723/wd/hub"
    apk_path = selected_machine["apk"]

    print(f"🚀 Running tests on: {selected_device} | Appium Server: {appium_url} | APK: {apk_path}")

    # Define Appium Desired Capabilities
    desired_caps = {
        "platformName": "Android",
        "appium:deviceName": "Android Device",
        "appium:automationName": "UiAutomator2",
        "appium:platformVersion": "15",  # Adjust based on available emulator
        "appium:app": apk_path,  
        "appium:noReset": True
    }

    try:
        # Initialize WebDriver with the correct Appium server (master/slave)
        driver = webdriver.Remote(command_executor=appium_url, desired_capabilities=desired_caps)
        driver.implicitly_wait(10)
    except Exception as e:
        pytest.fail(f"❌ ERROR: WebDriver initialization failed: {e}")

    request.cls.driver = driver  # Assign driver to test class
    yield driver
    driver.quit()

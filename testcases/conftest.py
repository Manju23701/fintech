import pytest
from appium import webdriver
import os

path = os.getcwd()


@pytest.fixture(scope='class')
def setup(request):
    desiredcapabilities = {
        "platformName": "Android",
        "deviceName": "Andriod Emulator",
        "app": "C:\\Users\\ManjulaAlagarsamy\\Downloads\\fin.apk",
        # #"automationName": "To Run the Complete Flow",
        # "appWaitActivity":"com.evstest.kidscustomerapp.HomeActivity",
        # "adbExecTimeout": 50000,
        "noReset": "true",
        "fullReset": "false"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcapabilities)

    driver.implicitly_wait(80)

    request.cls.driver = driver

    print('The Request is Accepted')



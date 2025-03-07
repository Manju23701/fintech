import time

from selenium.webdriver.common.by import By


skip = '//android.widget.Button[@content-desc="Skip"]'
done='//android.widget.Button[@content-desc="done"]'
reg='//android.view.View[@content-desc="Login/Register"]'
mobile='//android.widget.EditText[@content-desc="Mobile number"]'


class applyloanclass():

    def __init__(self,driver):
        self.driver = driver

    def applyloan(self):
        self.driver.find_element(By.XPATH,skip).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, done).click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,reg).click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,mobile).click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, mobile).send_keys("9000000000")
        # time.sleep(2)

        # self.driver.find_element(By.XPATH, continue_btn).click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, name).click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, name).send_keys("Manju")
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, mobile).click()
        # time.sleep(2)

        # self.driver.find_element(By.XPATH, verify).click()
        # time.sleep(2)
        #
        #
        #



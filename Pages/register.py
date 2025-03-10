import time

from selenium.webdriver.common.by import By

package="com.smiligence.smiligencehrportal:id/"
skip = '//android.widget.Button[@content-desc="Skip"]'
done='//android.widget.Button[@content-desc="done"]'
reg='//android.view.View[@content-desc="Login/Register"]'
mobile='//android.widget.EditText[@content-desc="Mobile number"]'
password=f"{package}edt_password"
phone=f"{package}edt_phoneNumber"
class applyloanclass():

    def __init__(self,driver):
        self.driver = driver

    def applyloan(self):
        self.driver.find_element(By.ID,phone).send_keys("9999999999")
        time.sleep(2)
        self.driver.find_element(By.ID, password).send_keys("Welcome@l1")
        time.sleep(2)
        # self.driver.find_element(By.XPATH, done).click()
        # time.sleep(2)
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



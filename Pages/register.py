import time

from selenium.webdriver.common.by import By

package="com.smiligence.smiligencehrportal:id/"

phone=f"{package}edt_phoneNumber"
password=f"{package}edt_password"
login_btn=f"{package}otpVerificationButton"
allow=f"{package}permission_allow_button"
class loginclass():

    def __init__(self,driver):
        self.driver = driver

    def login(self,mobile,password_):
        self.driver.find_element(By.ID,phone).send_keys(mobile)
        time.sleep(2)
        self.driver.find_element(By.ID, password).send_keys(password_)
        time.sleep(2)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.ID, login_btn).click()
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



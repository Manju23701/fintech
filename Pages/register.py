
from selenium.webdriver.common.by import By
import time

package ="com.smiligence.smiligencehrportal:id/"

phn_id = f"{package}edt_phoneNumber"

password_id =f"{package}edt_password"
login_id = f"{package}otpVerificationButton"




class loginclass():

    def __init__(self,driver):
        self.driver = driver

    def login(self,name,password):
        self.driver.find_element(By.ID,phn_id).send_keys(name)
        time.sleep(3)
        self.driver.find_element(By.ID,password_id).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID, login_id).click()
        time.sleep(3)

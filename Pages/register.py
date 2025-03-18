from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Explicit wait for elements

        # Define element locators
        package = "com.smiligence.smiligencehrportal:id/"
        self.phone = (By.ID, f"{package}edt_phoneNumber")
        self.password = (By.ID, f"{package}edt_password")
        self.login_btn = (By.ID, f"{package}otpVerificationButton")
        self.allow_btn = (By.ID, f"{package}permission_allow_button")  # If needed

    def login(self, mobile, password_):
        # Wait for phone field and enter mobile number
        self.wait.until(EC.presence_of_element_located(self.phone)).send_keys(mobile)

        # Wait for password field and enter password
        self.wait.until(EC.presence_of_element_located(self.password)).send_keys(password_)

        # Click on login button
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
        print("Login process completed.")

        # # If there's a permission popup, allow it (Optional)
        # try:
        #     allow_element = self.wait.until(EC.element_to_be_clickable(self.allow_btn))
        #     allow_element.click()
        # except:
           

        

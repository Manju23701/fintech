import time

from selenium.webdriver.common.by import By

package="com.smiligence.smiligencehrportal:id/"
allow="com.android.permissioncontroller:id/permission_allow_button"
checkin_btn=f"{package}checkin_Button"
camera="com.android.camera2:id/shutter_button"
done="com.android.camera2:id/done_button"
checkinconfirm=f"{package}imagecheckin_button"
allow_permission="com.android.permissioncontroller:id/permission_allow_foreground_only_button"

reason_=f"{package}reason_edittextview"
checkin_next=f"{package}imagecheckin_button"
attention=f"{package}attention"
confirmcheckin=f"{package}conform_checkin_button"
burger_menu='//android.widget.ImageButton[@content-desc="Open navigation drawer"]'
logout='//android.widget.CheckedTextView[@resource-id="com.smiligence.smiligencehrportal:id/design_menu_item_text" and @text="Logout"]'

class checkinclass():

    def __init__(self,driver):
        self.driver = driver

    def checkin(self):
        self.driver.find_element(By.ID, allow).click()
        time.sleep(4)
        self.driver.find_element(By.ID,checkin_btn).click()
        time.sleep(4)
        self.driver.find_element(By.ID, camera).click()
        time.sleep(4)
        self.driver.find_element(By.ID, done).click()
        time.sleep(4)
        self.driver.find_element(By.ID, checkinconfirm).click()
        time.sleep(4)
        self.driver.find_element(By.ID, allow_permission).click()
        time.sleep(4)
        self.driver.find_element(By.ID, checkin_next).click()
        time.sleep(3)
        self.driver.find_element(By.ID, reason_).send_keys("Yes")
        time.sleep(3)
        # self.driver.find_element(By.ID, attention).send_keys("Yes")

        self.driver.find_element(By.ID, confirmcheckin).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, burger_menu).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, logout).click()
        time.sleep(3)

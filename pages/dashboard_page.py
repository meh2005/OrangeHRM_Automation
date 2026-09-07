from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    user_dropdown = (
        By.XPATH,
        "//span[contains(@class,'oxd-userdropdown-tab')]"
    )

    logout = (
        By.XPATH,
        "//a[text()='Logout']"
    )

    def logout_user(self):

        self.wait.until(
            EC.element_to_be_clickable(self.user_dropdown)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.logout)
        ).click()
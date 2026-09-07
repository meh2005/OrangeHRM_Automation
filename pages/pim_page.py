from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    pim_menu = (By.XPATH, "//span[text()='PIM']")
    add_employee = (By.XPATH, "//a[text()='Add Employee']")

    def go_to_pim(self):

        pim = self.wait.until(
            EC.visibility_of_element_located(self.pim_menu)
        )

        # Mouse hover over PIM and click
        ActionChains(self.driver).move_to_element(pim).click().perform()

    def click_add_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(self.add_employee)
        ).click()
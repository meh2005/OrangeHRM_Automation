from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    first_name = (By.NAME, "firstName")
    middle_name = (By.NAME, "middleName")
    last_name = (By.NAME, "lastName")

    employee_id = (
        By.XPATH,
        "//label[text()='Employee Id']/parent::div/following-sibling::div//input"
    )

    save_button = (By.XPATH, "//button[@type='submit']")

    form_loader = (By.CLASS_NAME, "oxd-form-loader")

    def add_employee(self, first, middle, last, emp_id):

        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first)

        self.wait.until(
            EC.visibility_of_element_located(self.middle_name)
        ).send_keys(middle)

        self.wait.until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last)

        # Employee ID
        emp_field = self.wait.until(
            EC.visibility_of_element_located(self.employee_id)
        )

        # Select the automatically generated ID
        emp_field.click()
        emp_field.send_keys(Keys.CONTROL, "a")
        emp_field.send_keys(Keys.BACKSPACE)

        # Enter our Employee ID
        emp_field.send_keys(emp_id)

        # Verify that the correct ID is actually present
        self.wait.until(
            lambda driver: emp_field.get_attribute("value") == emp_id
        )

        # Wait for any form loader to disappear
        self.wait.until(
            EC.invisibility_of_element_located(self.form_loader)
        )

        # Click Save
        save = self.wait.until(
            EC.element_to_be_clickable(self.save_button)
        )

        save.click()
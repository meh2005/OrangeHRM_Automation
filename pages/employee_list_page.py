from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeListPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    employee_list = (
        By.XPATH,
        "//a[text()='Employee List']"
    )

    def go_to_employee_list(self):
        self.wait.until(
            EC.element_to_be_clickable(self.employee_list)
        ).click()

    def verify_employee(self, first_name, last_name, emp_id):

        # Find employee row using Employee ID
        row = (
            By.XPATH,
            f"//div[@role='row'][.//*[normalize-space()='{emp_id}']]"
        )

        try:
            employee_row = self.wait.until(
                EC.visibility_of_element_located(row)
            )

            row_text = employee_row.text

            print(f"Checking: {first_name} {last_name} ({emp_id})")
            print(f"Row: {row_text}")

            if first_name in row_text and last_name in row_text:
                print(f"{first_name} {last_name} - Name Verified")
                return True

            print(f"{first_name} {last_name} - Name Not Verified")
            return False

        except Exception as e:
            print(f"{first_name} {last_name} - Name Not Verified")
            print("Error:", e)
            return False
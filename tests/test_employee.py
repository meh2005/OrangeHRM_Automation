from selenium import webdriver

from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.employee_page import EmployeePage
from pages.employee_list_page import EmployeeListPage
from pages.dashboard_page import DashboardPage


def test_add_employees():

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        # Login
        driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")

        # Navigate to PIM
        pim_page = PIMPage(driver)
        pim_page.go_to_pim()

        employees = [
            ("Auto", "Test", "One", "AT260901"),
            ("Auto", "Test", "Two", "AT260902"),
            ("Auto", "Test", "Three", "AT260903"),
            ("Auto", "Test", "Four", "AT260904")
        ]

        # Add employees
        for first, middle, last, emp_id in employees:

            pim_page.click_add_employee()

            employee_page = EmployeePage(driver)

            employee_page.add_employee(
                first,
                middle,
                last,
                emp_id
            )

            pim_page.go_to_pim()

        print("4 Employees Added Successfully")

        # Navigate to Employee List
        employee_list_page = EmployeeListPage(driver)
        employee_list_page.go_to_employee_list()

        # Verify added employees
        for first, middle, last, emp_id in employees:
            assert employee_list_page.verify_employee(first, last, emp_id)

        # Navigate to Dashboard
        driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        )

        # Logout
        dashboard_page = DashboardPage(driver)
        dashboard_page.logout_user()

        # Verify logout
        assert "/auth/login" in driver.current_url

        print("Logout Successful")

    finally:
        driver.quit()
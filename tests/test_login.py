from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_login():

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        login_page = LoginPage(driver)

        login_page.login("Admin", "admin123")

        WebDriverWait(driver, 30).until(
            EC.url_contains("/dashboard")
        )

        assert "/dashboard" in driver.current_url

    finally:
        driver.quit()
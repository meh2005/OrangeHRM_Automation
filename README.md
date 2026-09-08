# OrangeHRM QA Engineer Assignment 2026

## Project Overview

This project contains manual testing documentation and Selenium automation for the OrangeHRM demo application.

The automation is implemented using Python, Selenium WebDriver, PyTest, and the Page Object Model (POM).

## Tools & Technologies

- Python 3
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Google Chrome
- Git & GitHub

## Automation Scope

The automated test suite covers:

1. OrangeHRM login
2. Navigation to the PIM module
3. Mouse hover and click on PIM
4. Adding 4 employees
5. Navigating to Employee List
6. Verifying the names of the added employees
7. Logout from the Dashboard

## Project Structure

```text
OrangeHRM_Automation/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── employee_page.py
│   ├── employee_list_page.py
│   └── pim_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_employee.py
│
├── .gitignore
└── README.md

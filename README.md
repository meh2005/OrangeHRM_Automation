# OrangeHRM QA Engineer Assignment 2026



\## Project Overview



This project contains manual testing documentation and Selenium automation for the OrangeHRM demo application.



The automation is implemented using Python, Selenium WebDriver, PyTest, and the Page Object Model (POM).



\## Tools \& Technologies



\- Python 3

\- Selenium WebDriver

\- PyTest

\- Page Object Model (POM)

\- Google Chrome

\- Git \& GitHub



\## Automation Scope



The automated test suite covers:



1\. OrangeHRM login

2\. Navigation to the PIM module

3\. Mouse hover and click on PIM

4\. Adding 4 employees

5\. Navigating to Employee List

6\. Verifying the names of the added employees

7\. Logout from the Dashboard



\## Project Structure



```text

OrangeHRM\_Automation/

│

├── pages/

│   ├── \_\_init\_\_.py

│   ├── login\_page.py

│   ├── dashboard\_page.py

│   ├── employee\_page.py

│   ├── employee\_list\_page.py

│   └── pim\_page.py

│

├── tests/

│   ├── \_\_init\_\_.py

│   ├── test\_login.py

│   └── test\_employee.py

│

├── .gitignore

└── README.md


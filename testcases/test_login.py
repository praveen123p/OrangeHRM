
from pages.loginpage import LoginPage
from pages.add_employee import AddEmployeePage
from pages.verify_employees import EmployeeListPage
import time


class Test_01_Admin_login:

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    inv_pw = "wropassword"
    blank = " "

    def test_method(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.enter_un(self.username)
        self.lp.enter_pw(self.password)
        self.lp.click_login()

    def test_valid_login(self,setup):
        self.test_method(setup)
        time.sleep(2)


    def test_invalid_password(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.enter_un(self.username)
        self.lp.enter_pw(self.inv_pw)
        self.lp.click_login()
        time.sleep(1)


    def test_blank_fields(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.enter_un(self.blank)
        self.lp.enter_pw(self.blank)
        self.lp.click_login()
        time.sleep(1)

    def test_navigate_to_pim(self,setup):
        self.test_method(setup)
        time.sleep(5)
        self.lp.go_to_pim()
        time.sleep(2)
        # Step 3: Validate navigation
        assert "pim" in self.driver.current_url.lower()

    def test_add_multiple_employees(self,setup):
        self.test_method(setup)
        time.sleep(5)
        self.lp.go_to_pim()
        time.sleep(2)
        self.emp = AddEmployeePage(self.driver)
        # Employee Data
        employees = [
            {"first_name": "praveen", "last_name": "kumar"},
            {"first_name": "virat", "last_name": "kohli"},
            {"first_name": "test", "last_name": "user"},
            {"first_name": "man", "last_name": "manual"},
        ]
        # Step 3: Add Employees
        for emp_data in employees:
            self.emp.click_add_employee()
            time.sleep(1)
            self.emp.add_employee(emp_data["first_name"], emp_data["last_name"])
            time.sleep(2)  # Wait for employee to save

    def test_verify_employees(self, setup):
        self.test_method(setup)
        time.sleep(5)
        self.lp.go_to_pim()
        time.sleep(2)
        self.el = EmployeeListPage(self.driver)
        self.el.click_employee_list()
        # List of employees previously added
        employees = [
            {"first_name": "praveen", "last_name": "kumar"},
            {"first_name": "virat", "last_name": "kohli"},
            {"first_name": "test", "last_name": "user"},
            {"first_name": "man", "last_name": "manual"},
        ]

        for emp in employees:
            full_name = f"{emp['first_name']} {emp['last_name']}"
            self.el.search_employee(full_name)
            found = self.el.verify_employee(emp['first_name'], emp['last_name'])
            assert found, f"{full_name}: Name Not Found"
            print(f"{full_name}: Name Verified")

        time.sleep(1)
        self.el.logout()
        print("Logged Out")



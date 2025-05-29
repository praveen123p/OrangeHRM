from selenium.webdriver.common.by import By

class AddEmployeePage:

    add_employee_btn = "Add Employee"
    f_name = "firstName"
    l_name = "lastName"
    save_button = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def click_add_employee(self):
        self.driver.find_element(By.LINK_TEXT, self.add_employee_btn).click()

    def add_employee(self, first_name, last_name):
        self.driver.find_element(By.NAME, self.f_name).send_keys(first_name)
        self.driver.find_element(By.NAME, self.l_name).send_keys(last_name)

        self.driver.find_element(By.XPATH, self.save_button).click()
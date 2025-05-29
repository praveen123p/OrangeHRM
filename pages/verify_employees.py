from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.wait import WebDriverWait


class EmployeeListPage:


    employee_list_link = "Employee List"
    search_name_xpath = "(//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active'])[1]/input"
    search_button = "//button[@type='submit']"
    user_menu = "oxd-userdropdown-name"
    logout_button = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def click_employee_list(self):
        self.driver.find_element(By.LINK_TEXT, self.employee_list_link).click()

    def search_employee(self, name):
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.element_to_be_clickable((By.XPATH, self.search_name_xpath)))
        search_input.clear()
        search_input.send_keys(name)
        time.sleep(1)  # Wait for hints
        search_input.send_keys(Keys.ENTER)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.search_button))).click()
        time.sleep(2)  # Wait for results

    def verify_employee(self, first_name, last_name):
        full_name = f"{first_name} {last_name}"
        wait = WebDriverWait(self.driver, 10)
        rows = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")))

        for row in rows:
            print("ROW TEXT :: ")
            print(row.text.lower().replace("\n", " "))
            if full_name.lower() in row.text.lower().replace("\n", " "):
                return True
        return False

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, self.user_menu).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.logout_button).click()

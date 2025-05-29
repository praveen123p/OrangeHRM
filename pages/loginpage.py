from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class LoginPage:

    username_xpath = "//input[@placeholder='Username']"
    password_xpath = "//input[@placeholder='Password']"
    xpath_login = "//button[@type='submit']"
    pim_xpath = "//span[text()='PIM']"


    def __init__(self, driver):
        self.driver = driver

    def enter_un(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enter_pw(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.xpath_login).click()

    def go_to_pim(self):
        actions = ActionChains(self.driver)
        pim_element = self.driver.find_element(By.XPATH, self.pim_xpath)
        actions.move_to_element(pim_element).click().perform()

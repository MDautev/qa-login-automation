from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "submit")

    def load(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


    def get_error_message(self):
        try:
            error_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "error"))
            )
            return error_element.text
        except:
            return "[NO ERROR ELEMENT]"




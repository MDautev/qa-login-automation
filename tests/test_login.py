from pages.login_page import LoginPage
import time

def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_login()

    time.sleep(1)

    success_message = driver.find_element("tag name", "h1").text
    assert success_message == "Logged In Successfully"

def test_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.enter_username("student")
    login_page.enter_password("WrongPassword")
    login_page.click_login()

    time.sleep(1)

    error = login_page.get_error_message()
    assert "invalid" in error.lower()

def test_empty_username(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.enter_username("")
    login_page.enter_password("Password123")
    login_page.click_login()

    time.sleep(1)

    error = login_page.get_error_message()
    assert "invalid" in error.lower()

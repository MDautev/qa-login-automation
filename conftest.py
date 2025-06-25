import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Setup: стартиране на браузъра
    driver = webdriver.Chrome()
    yield driver
    # Teardown: затваряне на браузъра
    driver.quit()

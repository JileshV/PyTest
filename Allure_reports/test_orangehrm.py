import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

class TestHRM:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        time.sleep(6)

    def teardown_method(self):
        self.driver.quit()

    def test_logo(self):
        status = self.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
        assert status

    def test_listEmployees(self):
        pytest.skip('Skipping for now')

    def test_login(self):
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        time.sleep(5)
        user = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").text
        print(user)
        assert user == "test123 test123"
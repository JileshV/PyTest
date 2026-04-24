import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup_and_teardown(request):       #setup_module runs setup before test run and teardown after all tests are run
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
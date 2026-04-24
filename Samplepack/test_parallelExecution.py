import time
import pytest

# def setup_function(function):       #setup_module runs setup before test run and teardown after all tests are run
#     print("SETUP FUNCTION")
# def teardown_function(function):    #teardown_module runs setup before test run and teardown after all tests are run
#     print("TEARDOWN FUNCTION")

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch():
    def test_one(self):
        self.driver.get("https://omayo.blogspot.com/")
        time.sleep(5)
        print("Done")

    def test_tutorials(self):
        self.driver.get("https://tutorialsninja.com/demo/")
        time.sleep(5)
        print("Done")

    def test_selenium143(self):
        self.driver.get("https://selenium143.blogspot.com/")
        time.sleep(5)
        print("Done")

    def test_selenium_by_arun(self):
        self.driver.get("https://selenium-by-arun.blogspot.com/")
        time.sleep(5)
        print("Done")

    def test_jquery(self):
        self.driver.get("https://jqueryui.com/")
        time.sleep(5)
        print("Done")

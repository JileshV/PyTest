import time
from selenium import webdriver

def setup_function(function):       #setup_module runs setup before test run and teardown after all tests are run
    print("SETUP FUNCTION")
def teardown_function(function):    #teardown_module runs setup before test run and teardown after all tests are run
    print("TEARDOWN FUNCTION")

def test_one():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")
    time.sleep(5)
    print("Done")
    driver.quit()

def test_tutorials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(5)
    print("Done")
    driver.quit()

def test_selenium143():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium143.blogspot.com/")
    time.sleep(5)
    print("Done")
    driver.quit()

def test_selenium_by_arun():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium-by-arun.blogspot.com/")
    time.sleep(5)
    print("Done")
    driver.quit()

def test_jquery():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/")
    time.sleep(5)
    print("Done")
    driver.quit()

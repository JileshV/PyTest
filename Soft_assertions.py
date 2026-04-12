import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_tutorials_ninja():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(5)
    expected_title = "Your Store xyz"
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    time.sleep(5)
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_enabled()
    driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver import ActionChains, Keys


@pytest.fixture
def setUp():
    global driver,product
    product = input("Enter the product to be searched")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_check(setUp):
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("flipkart")
    time.sleep(1)
    driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    driver.find_element_by_name("q").send_keys(product)
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
    time.sleep(1)
    action = ActionChains(driver)
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).click()
    driver.execute_script("window.scrollTo(0,window.scrollY + 1200)")
    time.sleep(5)
    action.click()
    time.sleep(10)



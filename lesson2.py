from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR ,"#answer")
    input1.send_keys(y)


    option1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option2.click()


    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    
    x_element = browser.find_element(By.CSS_SELECTOR, "img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    print(y)
    result= browser.find_element(By.ID, "answer")
    result.send_keys(y)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    radio1 = browser.find_element(By.ID, "peopleRule")
    radio1.click()

    radio2 = browser.find_element(By.ID, "robotsRule")
    radio2.click()

    btn = browser.find_element(By.CSS_SELECTOR, "button")
    btn.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

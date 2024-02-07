from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, "button")
    btn.click()
    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    result= browser.find_element(By.ID, "answer")
    result.send_keys(y)
    
    btn = browser.find_element(By.CSS_SELECTOR, "button")
    btn.click()
finally:
# успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
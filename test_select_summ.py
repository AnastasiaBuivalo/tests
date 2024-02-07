from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")

    print(num1)
    select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_value(str(int(num1.text)+int(num2.text)));

    btn = browser.find_element(By.CSS_SELECTOR, "button")
    btn.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
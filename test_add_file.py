from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input.form-control")
    for element in elements:
        element.send_keys("Мой ответ")
   
    file = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname("1"))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
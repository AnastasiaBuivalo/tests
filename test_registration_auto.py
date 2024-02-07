from selenium import webdriver
from selenium.webdriver.common.by import By
import time


import unittest

def search_click_required_fields(link):
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']/div[@class='form-group first_class']/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']/div[@class='form-group second_class']/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']/div[@class='form-group third_class']/input")
        input3.send_keys("Petrov")
        
        time.sleep(10)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text

#наследуемся от класса TestCase
class TestRequiredFields(unittest.TestCase):
    
    
    #self-ссылка на экземпляр класса
    def test_url1(self):
        link = "http://suninjuly.github.io/registration1.html"
        
        self.assertEqual("Congratulations! You have successfully registered!", search_click_required_fields(link))
            # ожидание чтобы визуально оценить результаты прохождения скрипта
    
    def test_url2(self):
        link = "http://suninjuly.github.io/registration2.html"
        
        self.assertEqual("Congratulations! You have successfully registered!", search_click_required_fields(link))
            # ожидание чтобы визуально оценить результаты прохождения скрипта

    
        
if __name__ == "__main__":
    unittest.main()




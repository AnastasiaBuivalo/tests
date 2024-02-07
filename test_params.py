
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

class TestAutorise():  
    string=""
    links = [
        # "https://stepik.org/lesson/236895/step/1",
        # "https://stepik.org/lesson/236896/step/1",
        # "https://stepik.org/lesson/236897/step/1",
        # "https://stepik.org/lesson/236898/step/1",
        # "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1"
        "https://stepik.org/lesson/236904/step/1",
        # "https://stepik.org/lesson/236905/step/1"
    ]
    @pytest.mark.parametrize('link', links)
    def test_autorise(self, browser, link):
        #отркытие ссылки
        browser.get(link)
        browser.implicitly_wait(10)

        #hgеход к форме входа
        btnLogin = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()

        #вход
        login = browser.find_element(By.ID, "id_login_email")
        login.send_keys("abuyvalo@mail.ru")
        password = browser.find_element(By.ID, "id_login_password")
        password.send_keys("dbyrc3010")
        button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
        button.click()

        #ввод ответа
        result = browser.find_element(By.CSS_SELECTOR, "textarea")
        time.sleep(15)
        result.send_keys(str(math.log(int(time.time()))))

        #ожидание кноки отправки
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()
        time.sleep(15)

        answ = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        try:
            assert "Correct!" in answ.text, f"{answ.text}"
        except AssertionError:
            self.string += answ


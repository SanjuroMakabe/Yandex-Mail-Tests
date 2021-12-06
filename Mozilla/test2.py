import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class YandexMailWrongPass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(
            executable_path=r'.\ffdriver\geckodriver.exe'
        )

    def test_yandex_auth(self):
        driver = self.driver
    #логин и пароль пользователя        
        login='SanjuroTest'
        password='ue93n2d7hgt3-51'
    #переходим на стартовую страницу и нажимаем по первой кнопке "Войти"       
        driver.get("https://mail.yandex.ru/")
        time.sleep(1)
        clickenter = driver.find_element(By.XPATH, '//*[@id="index-page-container"]/div/div[2]/div/div/div[4]/a[2]')
        time.sleep(1)
        clickenter.click()
        time.sleep(1) 
    #нажимаем по полю с логином и вводим
        loginform = driver.find_element(By.XPATH, '//*[@id="passp-field-login"]')
        time.sleep(1)
        loginform.send_keys(login)
        time.sleep(1)   
    #нажимаем по второй кнопке "Войти"
        clickenter2 = driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
        time.sleep(1)
        clickenter2.click()
        time.sleep(1) 
    #нажимаем по полю с паролем и вводим неверный
        passform = driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]')
        passform.click()
        passform.send_keys(password)
        time.sleep(1)
        
    #нажимаем по третьей кнопке "Войти"
        auth_button = driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
        auth_button.click()
        time.sleep(1)
        
    #удостоверяемся в появлении предупреждения, что пароль - неверный
        auth_warning = driver.find_element(By.XPATH, '//*[@id="field:input-passwd:hint"]')
        print('***ПАРОЛЬ НЕВЕРНЫЙ***')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
    
    
import unittest,time
from selenium import webdriver

class TestCaseReg(unittest.TestCase):#继承unittest，固定用法。




    def test_01_regist_success(self):
        driver=webdriver.Chrome(executable_path='drivers\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://132.232.44.158:8080/ljindex/')
        driver.find_element_by_link_text('注册').click()
        time.sleep(3)   #以上都是用selenium使用driver驱动打开并控制网页
        driver.quit()

        #

    




    
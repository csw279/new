#类来实现测试用例

import unittest,time
from selenium import webdriver

# 这个类 就是一个 登录功能的模块，里面存放的所有的  def成员方法  则是具体的每个测试用例
class TestCaseLogin(unittest.TestCase):

    #每个成员方法就是固定的测试用例
    def test_01_login_success(self):
        driver=webdriver.Chrome(executable_path='drivers\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://132.232.44.158:8080/ljindex/')
        time.sleep(3)
        driver.find_element_by_link_text('登录').click()
        time.sleep(3)

        driver.find_element_by_id('username').send_keys('liuyun1')
        driver.find_element_by_id('password').send_keys('a12345678')
        driver.find_element_by_id('userLogin').click()

        #断言
        time.sleep(3)
        assert driver.title =='测谈网'

    def test_02(self):
        assert 1==2
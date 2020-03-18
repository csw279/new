import time
import traceback
from selenium import webdriver
from seleniumtools import find_element # 用的自定义的动态查找方法


driver = webdriver.Chrome(executable_path="F:\\Vscode   file\\study code\\seleniumtest\\chromedriver.exe")##大写的c
driver.maximize_window()
driver.get("http://132.232.44.158:8080/ljindex/index.html")

username = ("id", "username")                                   # 用户名输入框
phonenum = ("id", "phonenum")                                   # 电话输入框
password = ("id", "password")                                   # 密码输入框
confirpw = ("id", "confirpw")                                   # 确认密码输入框
emailnum = ("id", "emailnum")                                   # 邮箱输入框
userRegist = ("id", "userRegist")                               # 注册按钮
 # userregs = ("xpath", '//*[@id="unlogin"]/div[2]/a')             # 注册页面按钮
userregs = ("link text", '注册')             # 注册页面按钮

find_element(driver, userregs).click()                          # 点击注册按钮
find_element(driver, username).send_keys("aaa22441")             # 输入用户名
find_element(driver, password).send_keys("a123456")             # 输入密码
find_element(driver, confirpw).send_keys("a123456")             # 确认密码
find_element(driver, phonenum).send_keys("13690777862")         # 输入电话
find_element(driver, emailnum).send_keys("liuy4417@qq.com")      # 输入邮箱
find_element(driver, userRegist).click()                        # 点击注册 

time.sleep(3)
driver.switch_to.alert.accept()         #定位网页弹窗#driver.switch_to.alert()    再用.accept()  接收返回的网页信息，
#断言开始，这用于判断测试用例是否通过。
#获取并对比.accept()里的信息，
time.sleep(3)
try:
    assert driver.current_url =='http://132.232.44.158:8080/ljindex/html/login.html'
    print('注册成功')
except:
    traceback.print_exc()
    print('注册失败')
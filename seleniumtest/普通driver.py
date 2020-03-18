import time
import traceback
from selenium  import webdriver  #网页驱动
url='http://132.232.44.158:8080/ljindex'
driver=webdriver.Chrome(executable_path='F:\\Vscode   file\\study code\\dailywork\\chromedriver.exe')  #启动chrome.exe驱动插件driver
#  注意 Chrome 中的c是大写

#driver是那个驱动插件 用driver    get打开网址，window最大化，定位元素，点击元素对应的按钮click

driver.maximize_window()    #打开的界面最大化,window没有s
driver.get(url)              #打开网址
#开始进行元素定位
e=driver.find_element_by_xpath('//*[@id="unlogin"]/div[2]/a')   # 通过元素    定位   该注册按钮                     需要点F12打开开发者工具，查看元素，进行定位。
e.click()                   #点击元素

time.sleep(3)   #静态等待是   因为代码有时候运行太快，网页反应跟不上而报错

driver.find_element_by_id('username').send_keys('checa44271')
driver.find_element_by_id('phonenum').send_keys('15897945609')              #可将find_element    send_keys   封装起来
driver.find_element_by_id('password').send_keys('a111242333')
driver.find_element_by_id('confirpw').send_keys('a111242333')
driver.find_element_by_id('emailnum').send_keys('114348@qq.com')
driver.find_element_by_id('userRegist').click()
time.sleep(3)
driver.switch_to.alert.accept()         #定位网页弹窗#driver.switch_to_alert()    再用.accept()  接收返回的网页信息，
#断言开始，这用于判断测试用例是否通过。
#获取并对比.accept()里的信息，
try:
    assert driver.current_url =='http://132.232.44.158:8080/ljindex/html/login.html'
    print('注册成功')
except:
    traceback.print_exc()
    print('注册失败')
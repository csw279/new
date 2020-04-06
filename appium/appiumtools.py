from selenium.webdriver.support.ui import WebDriverWait
from appium import  webdriver   
import time

# 自定义的方法
def find_element(driver=None, locator=None, timeout=10):
    """
        名字：动态查找元素
        参数：
            driver: 浏览器的实例化对象
            locator: 元素定位的方法 ("id", "username") / ("xpath", "xxxxx") /("aid", "xxxxx") /("aui", "xxxxx")
                类型： 
                    ID = "id"
                    XPATH = "xpath"
                    accessibility_id = "aid"
                    android_uiautomator = "aui"
            timeout: 超时时间：默认10
    """

    if locator[0] == "aid":
        locator = ("accessibility id", locator[1])
    if locator[0] == "aui":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))

    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))


def click(driver, locator):
    find_element(driver, locator).click()


def is_exsit(driver, locator):
    try:
        find_element(driver, locator)
        return True
    except:
        return False

def send_keys(driver,locator,data):
    find_element(driver, locator).send_keys(data)

def get_driver(A,V,d,app,appA):
    """
        获取设备driver
    """
    desired_caps = {}
    desired_caps['platformName'] = A              # 打开什么平台的app，固定的 > 启动安卓平台
    desired_caps['platformVersion'] = V           # 安卓系统的版本号：adb shell getprop ro.build.version.release
    desired_caps['deviceName'] = d                # 手机/模拟器的型号：adb shell getprop ro.product.model
    desired_caps['appPackage'] = app              # app的名字：
                                                        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                        # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
    desired_caps['appActivity'] = appA            # 同上↑
    desired_caps['unicodeKeyboard'] = True              # 为了支持中文
    desired_caps['resetKeyboard'] = True                # 设置成appium自带的键盘
    # 去打开app，并且返回当前app的操作对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver  ####  返回driver操作句柄


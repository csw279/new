from appium import webdriver
#from appiumtools import find_element, click, is_exsit



desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'sm-g9250'                # 手机/模拟器的型号：adb shell getprop ro.product.model 
                                                #型号和版本是确定手机的参数
desired_caps['appPackage'] = 'io.appium.android.apis'               # app的名字：
                                                        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                        # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '.ApiDemos'              # 同上↑   #得到包名是确定软件的参数
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) # 打开指定手机里面的软件；driver=定位软件的句柄


#  driver.find_element_by_accessibility_id('Accessibility').click()#accessbility  id
#  driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Custom View"]').click()#xpath
#     尽量用这两种方法定位元素。

#  driver.find_element_by_id('android:id/text1').click()#  id是  resource id      #一般不用，    因为resource id不唯一

driver.find_element_by_android_uiautomator('new UiSelector().text("App")').click()   # 通过文本值，与selenium不同，那个文本值只能定义超链接，这里直接定义文本就行了
                                                                  #    最轻松简单的方法

driver.find_element_by_android_uiautomator('new UiSelector().text("Search")')


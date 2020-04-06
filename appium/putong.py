import time
from appiumtools import find_element,get_driver

driver=get_driver('Android','5.1.1','xiaomi 8','io.appium.android.apis','.ApiDemos')

####  定位元素首选 by_aui(文本值),by_xpath,by_aid(accessbility_id)  这三种
####   by_id 是根据resource_id来的
a=('aid','Accessibility')
b=('xpath','/hierarchy/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.View[1]')
c=('aui','Custom View')
find_element(driver,a).click()
find_element(driver,c).click()
find_element(driver,b).click()
# find_element(driver,b).send_keys('aaa')
try:
    assert driver.current_activity=='.accessibility.CustomViewAccessibilityActivity'
    print('测试成功')
except:
    print('测试失败')
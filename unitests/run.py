###整个框架的运行入口

import unittest
from utils.HTMLTestRunner import HTMLTestRunner      #因为有__init__.py文件，所以是个包

#1,加载所有的测试用例

#使用unittest自带的loader加载器去动态查找   ‘cases文件夹’  下面的以 ‘test_开头，.py结尾’ 的测试用例
t=unittest.defaultTestLoader.discover('cases','test_*.py')#unittest规定的

#2，直接运行所有的测试用例，并且自动生成测试报告

title='测试报告'
descr='测试报告描述'
report='./reports/report.html'  #网页后缀名

with open(report,'wb') as f:   #创建report变量路径里面的一个文件，如果存在则替换，不存在则新建
    runner=HTMLTestRunner(stream=f,title=title,description=descr)       #初始化HTMLTestRunner
    runner.run(t)                                                      #使用run方法运行所有的测试用例
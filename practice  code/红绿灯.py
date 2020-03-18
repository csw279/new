
import time                                 #python自带的包


dlist={'红':30,'绿':30,'黄':2}

for i in dlist:                             #遍历取字典取得是key值
    for j in range(dlist[i]):               #用键值法取value值这些数字，再用遍历，range数列生成器取这些数字
        time.sleep(1)
        #该指令表示使用time包里的sleep方法，功能为程序没运行一次就暂停一秒.
        print('{}灯已运行{}秒'.format(i,j))

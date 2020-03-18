
###  造数据
zh=[]

for i in range(1,1000):                    ##左闭右开原则
    username='csw{}'.format(1000+i)        ## format 格式化连接字符串
    password='asd4445'  
    emali='asd{}@qq.com'.format(1000+i)   
    phone=15944657892+i                    ##因为是数字，可以直接运算。
    zh.append('{},{},{},{}\n'.format(username,password,emali,phone))
    # break运行一个测试下


with open('C:\\Users\\Administrator\\Desktop\\黑马资源\\csw.txt','w+') as f:###在这个路径下有这个文件夹就添加数据，没这个就新建一个然后添加数据。
    for i in zh:
        f.write(i)

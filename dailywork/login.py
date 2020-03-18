from logindb import DBtool  #应用设计好的类，来实现与mysql数据库通信，注册功能
#注册
def register(username,password):
    if username == '' or password == '':
        return None #print('用户名或者密码不能为空！')  

    db=DBtool()
    sql = "select * from user where username = '{}'".format(username)
    res = db.query(sql)
    '''if res ==False:         #查询数据库失败了，查询语句有问题此时。     可有可没有
        
        return False    #注册失败
    else:'''
    if len(res) == 0:    #查询出来一个空的tuple，即没查到东西，
        sql1="insert into user values('{}','{}')".format(username,password)
        db.commit(sql1)  #此时添加数据，进行注册。
        return True
    else:
        return False   #查询出来一个嵌套的tuple，即查到东西了，已存在，所以报错注册失败。
                        
un = input('请输入用户名：')
pw = input('请输入密码：')
res = register(un,pw)
if res ==None :
    print('用户名或者密码不能为空！')
elif res ==False:
    print('用户名已存在，注册失败!')
else:
    print('注册成功!')
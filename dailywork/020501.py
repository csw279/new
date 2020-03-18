#login
a=input('请输入用户名:')
b=input('请输入密码:')
db=[{"username":"chen","password":"123"}]
if a=='' or b=='':
    print('不能有空值')
    exit()
else:
    for zhanghao in db:
        if zhanghao['username']==a:
            print('用户已存在')
            exit()
x={"username":a,"paaword":b}
db.append(x)
print(db)
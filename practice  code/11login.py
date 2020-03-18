a=input('请输入用户名:')
b=input('请输入密码:')

if a=='' or b =='':
    print('输入不能有空值')
    exit()

db={"username":"123","password":"123"}

if a != db["username"]:
    print('用户名错误')
elif b !=db["password"]:
    print('密码错误')
else:
    print('登录成功')
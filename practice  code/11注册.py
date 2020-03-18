db=[{"username":"张三","password":"123"},{"username":"李四","password":"123"},{"username":"赵五","password":"123"},{"username":"王六","password":"123"}]
u=input('请输入用户名:')
p=input('请输入密码:')

if u=='' or p=='':
    print('用户名或密码不可为空')
    exit()

for user in db :                 ###用遍历取列表里数据
    if user.get("username")==u:
        print('该用户名已存在')
        exit()

#如果执行到这里，遍历取了列表的值(字典)，没有发现重复username，那就添加注册的数据到数据库里面去。

x={"username":"","password":""}     ###有这个键值对那么就修改，没有则相当于添加新的元素。  字典{}元素的添加与修改是同种方法，具体看元素本身是否存在
x["username"]=u
x["password"]=p

db.append(x)
print(db)

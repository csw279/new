import  requests

u='http://www.test.com/login'
A=input('请输入用户名:')
B=input('请输入密码:')
d={'username':A,'password':B}

res=requests.post(url=u,json=d)             ## res 是 post请求 返回的响应值 

try:
    assert  res.status_code==200
    assert  res.json().get("status")==200
    print('登录成功')
except:
    print('登录失败')

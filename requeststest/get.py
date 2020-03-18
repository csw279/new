import requests

url='http://www.baidu.com'
res=requests.get(url)   ###返回 url 或者 接口所指向的资源，即get请求。
print(res.text)         ###将返回的数据提取其text。

###  res是返回的数据
try:
    assert res.status_code==200                    #属性方法status_code，获取res里面的http状态码
    assert res.json().get("status")==200           #先用json方法提取res里面的字典型数据，再用get方法，获取'status'键对应的值200。   
    print('测试通过') 
except:
    print('测试失败')                                                                             

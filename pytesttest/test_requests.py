#导入pytest

import pytest
import requests
from db import DBtool 

#每个方法就是一个测试用例

def test_01_login():
    #构造请求
    u='http://192.144.148.91:2333/login'
    d={"username":"chenchen1", "password":"a1234567" }

    r=requests.post(url=u,json=d)
    #断言
    assert r.status_code==200
    assert r.json()['status']==200     #requsets请求回来的是字符串，用json把"""去掉，就变成了原来的字典了，再用键值对取值得到设计好的‘状态码’ 

    #查询数据库
    db=DBtool(host='192.144.148.91',user='ljtest',password='123456',db='ljtestdb')
    sql="select * from t_user where username='{}'".format(d['username'])
    r=db.query(sql)

    assert r!=False
    assert len(r)!=0
    print('测试通过')
    
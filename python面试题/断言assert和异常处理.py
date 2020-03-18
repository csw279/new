### assert()方法
### 断言成功则程序继续运行，断言失败则程序报错

### try:   except:  try下面的代码通过则正常运行，代码异常报错则运行except下面的代码  

a=5
assert a>2
print('测试通过')
try:
    assert a>8      ###断言失败直接报错
except:
    print('代码错误')



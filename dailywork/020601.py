#将一个字典输出为列表
result=[]


#注册方法封装

def zhuche(a,b):
    db=[{'username':'c','password':'123'}]
    i={}
    if a=='' or b=='':
        return '账号密码不可为空'    
    for x in db:
        if a == x['username']:
            return '注册失败，账号已存在'
        else:
            i={'username':a,'password':b}        
            db.append(i)
            return db
    

a=input('请输入账号:')
b=input('请输入密码:')
x=zhuche(a,b)
print(x)



from dbtools import DBTool

def zhuche(u,p):
    db=DBTool()
    sql ="select * from t_class where cname='{}'".format(u)
    sql2="insert into t_class(cname,teacher)values({},{})".format(u,p)
    res = db.query(sql)
    if u=='' or p=='':
        return None#'注册失败，账号或密码不能为空'
    if res == False:  #查询数据库失败 
        return False #注册失败
    else:
        if len(res)==0:
            db.commit(sql2)
            return '注册成功'
        else:
            return '注册失败，账号已存在'

            
u=input('请输入cname:')
p=input('请输入teacher:')
q=zhuche(u,p)
print(q)

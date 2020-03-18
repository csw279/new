import pymysql  #用pymysql来操控mysql数据库，用来设计制作一个类。
class DBtool():
    def __init__(self,host='192.168.242.129',user='root',password='123456',db='test'):
        self.db = db
        self.host = host
        self.user = user
        self.password = password
      
    def query(self,sql):
        #try:
            db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
            cursor = db.cursor()
            cursor.execute(sql)     #执行查询语句
            res = cursor.fetchall() #获取查询结果
            db.close()              #关闭连接
            return res
        #except:
            #return False

    def commit(self,sql):
        try:
            db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
            cursor = db.cursor()
            cursor.execute(sql)     #执行查询语句
            db.commit()             #提交修改
            db.close()              #关闭连接
            return res
        except:
            return False

#体现了try的重要性，即，，判断语句问题。
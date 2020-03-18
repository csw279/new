db={'username':'123','password':'1234'}
x=[]
for i in db:#(for循环取值时虽然是取得元素，但是字典的键值段时分别取出来的，所以直接取得 键 key     当然db.keys()用这个方法也是可以的)
    x.append(i)
    x.append(db[i])
print(x)


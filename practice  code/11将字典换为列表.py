db={"username":"张三","password":"12345","sex":"男"}
x=[]
for result in db :
    x.append(result)
    x.append(db[result])

print(x)

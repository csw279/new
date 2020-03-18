sum=0
for i in range(100):
    if i %2 !=0:
        sum=sum+i
        print(sum)#在这里打印就是每循环一次就打印一次
    else:
        continue
 #倘若在这里打印，那么直接将所有循环后相加的和打印出来   
        
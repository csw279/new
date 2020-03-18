'''for i in range(1,10):
    for j in i:
        print(i,'x',j,'=',i*j)'''

for a in range(1,10):
    for b in range(1,a+1):
        print(a,'*',b,'=',a*b,end='\t')            #\t表示   程序每循环运行一次  就打印一个table，四个空格，一般用于制表
    print('')                                #这里表示和前面制表符错开，换个行，要不然有 end 在就不换行了
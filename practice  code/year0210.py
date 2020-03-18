x=[31,28,31,30,31,30,31,31,30,31,30,31]
a=input('请输入年份:')
b=eval(input('请输入月份:'))
c=eval(input('请输入日期:'))

sum=c

if eval(a)%4==0 and eval(a)%100!=0 or eval(a)%400==0:
    x[1]=29
for i in range(b-1):     # range(0)=[]  range(1)=[0] range(2)=[0,1]  把列表里所有的值取出来，print一次，去一次。
    sum=sum+x[i]
print('今天是',a,'年的第' ,sum,'天')
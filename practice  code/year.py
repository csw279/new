print('----------------------------------')
year=int(input("请输入年份:"))
month=int(input("请输入月份:"))
day=int(input("请输入日期:"))
monthlist=[31,28,31,30,31,30,31,31,30,31,30,31]
sum=day
if year % 4==0 and year % 100 !=0 or year % 400==0:# or 表示只要满足两方一个条件即可,即为闰年。
    monthlist[1]=29
    for i in range(month-1):#  range(0)=[]  range(1)=[0] range(2)=[0,1]  把列表里所有的值取出来，print一次，去一次。
        sum=sum+monthlist[i]
    #sum=sum+day
else :
    for i in range(month-1):
        sum=sum+monthlist[i]
    #sum=sum+day
print('今天是今年的第',sum,'天')

### for 循环加序列生成器
sum=0

for i in range(1,100,2):
    sum=sum+i
print(sum)


### while 循环
sum=0
a=1

while a<101:
    sum=sum+a
    a=a+2
print(sum)
    
###
sum = 0
n =1
while n < 100:
    if n % 2!=0:
        sum = sum + n
    n = n+1
print(sum)
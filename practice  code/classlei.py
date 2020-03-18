class Student():
    
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('{}:{}'.format(self.name,self.score))

    def get_grade(self):
        if self.score>=70:
            print('成绩良好')
        elif self.score>=60:
            print('成绩及格')
        else:
            print('成绩不及格')
#类的使用，实例化对象，  
a=input('请输入你的名字:')
b=eval(input('请输入成绩:'))
Grade=Student(a,b)#用Grade来实例化类class。

Grade.print_score()
Grade.get_grade()
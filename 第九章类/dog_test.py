''''创建多个实例'''
class Dog():
    def __init__(self,name,age):
        #初始化属性
        self.name=name
        self.age=age
    def sit( self ):
        print(self.name.title()+'issitting')
    def roll_over( self ):
        print(str(self.age)+':\trolled over')
my_dog=Dog('wille',6)#传参数
your_dog=Dog('luy',10)
print('my dogstr nameis'+my_dog.name.title()+'.')
print('my dog is age:'+str(my_dog.age)+':\tyears old')
my_dog.sit()#调用类中的方法
print('your_dog惊声尖叫：'+your_dog.name.title())
print('your_dog 多大了：'+str(your_dog.age))
your_dog.roll_over()
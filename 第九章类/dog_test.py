''''创建多个实例'''
class Dog():
    def __init__(self,name,age):
        #初始化属性
        self.name=name
        self.age=age
    def sit( self ):
        print(self.name.title()+'issitting')
    def roll_over( self ):
        print(self.age.title()+'rolled over')
my_dog=Dog('wille',6)
your_dog=Dog('luy',10)
print('my dogstr nameis'+my_dog.name.title()+'.')
print('my dog is age'+str(my_dog.age)+'years old')
my_dog.sit()

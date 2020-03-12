class dog():
    def __init__(self,name,age):#创建方法
        #初始化属性
        self.name=name
        self.age=age
    def sit( self ):
        print(self.name.title()+'is nowsitt')
    def roll_over( self ):
        print(self.name.title()+"roll")
dou_name=dog('lll','25')
# print(dou_name.roll_over(),dou_name.sit())
print(dou_name.name)#访问属性
dou_name.sit()#调用方法
dou_name.roll_over()


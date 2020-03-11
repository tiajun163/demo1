'''''创建car类'''
class Car():
    #创建函数 初始化属性
    def __init__( self,make,yearl,name,ord_dog ):
        self.make=make
        self.yearl=yearl
        self.name=name
        self.ord_dog=ord_dog
        self.read_odmometer=800
        #返回描述信息
    def Car_name( self ):
        car_names=self.make+'!'+self.yearl+'来'+self.name+\
                  self.ord_dog+str(self.read_odmometer)
        return car_names
    #将里程表设置为指定的值，禁止回调
    def get_des_name( self,mileage ):
        if mileage>=self.read_odmometer:
            self.read_odmometer=mileage
        else:
            print('禁止回调')
    #将里程表数增加指定的量
    def increment_odometer( self,milsages ):
        self.read_odmometer +=milsages
        #打印里程数
    def read_o( self ):
        print('里程数：'+str(self.read_odmometer))
my_user=Car('subaru', 'outback', '22013','GSG')
print(my_user.Car_name())
my_user.get_des_name(9000)
my_user.read_o()
my_user.increment_odometer(8000)
my_user.read_o()

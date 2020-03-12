class Car():
    #创建初始化属性方法
        def __init__(self,make ,model,year):
            self.make=make
            self.model=model
            self.year=year
            self.b_size=0#里程数
        #描述汽车的方法
        def get_descriptive_name( self ):
            long_name=str(self.year)+''+self.make+self.make
            return  long_name.title() #返回
        def read_odometer( self ):#汽车里程表
            print('汽车行驶的里程数：'+str(self.b_size))
        def update_odometer( self,mileage ):#更新里程数方法,且禁止把里程数往回调
            if mileage>self.b_size:
                self.mileage=mileage
            else:
                print("禁止往回调里程数")
        #将里程表读数增加到指定的量
        def increment_odometer( self,miles ):
            self.b_size +=miles
            print("里程数++")
        def fill_gas_tank(self):
            print("汽车有油箱")
class Battery():
    def __init__(self,b_size=80):
        self.b_size=b_size
    def descr_b( self ):
        print("电容量："+str(self.b_size))
        
class ElectricCar(Car):
    def __init__(self,make,model,year):
        ''''初始化父类属性0'''''
        super().__init__(make,model,year)
        self.b_y=Battery()
my_car=ElectricCar('ewh','dsa s','2020')
print(my_car.get_descriptive_name())
my_car.b_y.descr_b()
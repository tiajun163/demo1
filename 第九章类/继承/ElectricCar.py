class Car(object):
    #创建初始化属性方法
        def __init__(self,make ,model,year):
            self.make=make
            self.model=model
            self.year=year
            self.odometer=0#里程数
        #描述汽车的方法
        def get_descriptive_name( self ):
            long_name=str(self.year)+''+self.make+self.make
            return  long_name.title() #返回
        def read_odometer( self ):#汽车里程表
            print('汽车行驶的里程数：'+str(self.odometer))
        def update_odometer( self,mileage ):#更新里程数方法,且禁止把里程数往回调
            if mileage>self.odometer:
                self.mileage=mileage
            else:
                print("禁止往回调里程数")
        #将里程表读数增加到指定的量
        def increment_odometer( self,miles ):
            self.odometer +=miles
            print("里程数++")
        def fill_gas_tank(self):
            print("汽车有油箱")

class ElectricCar(Car):#继承Car类
      def __init__(self,make,model,year):
        #初始化父类的属性
         super().__init__(make,model,year)
         self.battery_size=70#创建子类的属性并初始化 电容量为70
      def describe_battery( self ):
         print('打印电瓶车的电容量：'+str(self.battery_size))

''''给子类定义属性和方法'''#''''重写父类方法'''
      # def fill_gas_tank():
      #     super().__init__(Car)
      #   print("电动车没油箱")

my_tesla=ElectricCar('tesla','model s','2020')#创建实例
print(my_tesla.get_descriptive_name())#打印
my_tesla.describe_battery()#调用的是子类的方法，实例
my_tesla.fill_gas_tank()#调用重写之后子类方法


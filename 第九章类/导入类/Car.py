''''可用的汽车类'''
class Cars():
    def __init__(self,make,model,year):
        #初始化属性
        self.make=make#汽车的品牌
        self.model=model#汽车类型
        self.year=year#年份
        self.odometer_reading=0#默认的里程数
        #描述汽车的方法
    def get_descriptive_name( self ):
        long_name=str(self.year)+'生产的'+self.make+self.model+'款！'
        return long_name
    #指出汽车的里程数
    def rad_odometer( self ):
        print('该汽车行驶了：'+str(self.odometer_reading)+"公里")
        #将里程表上的值设定为指定值，切不允许修改
    def update_odometer( self,mileage ):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("不允许修改行驶的里程数")
            #将里程表的读数增加到指定的量
    def increment_odometer( self,miles ):
        self.odometer_reading +=miles
   #创建一个电动汽车的类
class Battery():
   def __init__(self,battery_size=85):
       #初始化电动车属性
    self.battery_size=battery_size#
   def describe_battery( self ):
       #调用描述电瓶车容量的方法
       print('电瓶车的容量：'+str(self.battery_size)+'w')
   def get_range( self ):
       if self.battery_size==70:
           range=240
       elif self.battery_size==85:
           range=350
       message="电瓶车大概可以开："+str(range)+'公里'
       message+='火力全开'
       print(message)

class ElectricCar(Cars):
    # 继承父类
    def __init__(self,make,model,year):
        #初始化父类属性
        super().__init__(make,model,year)
        self.battery = Battery()
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
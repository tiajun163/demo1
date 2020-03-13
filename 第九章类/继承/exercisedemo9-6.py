'''''创建一个冰淇淋服务站'''
class Restaurant():
    #初始化类属性
    def __init__(self,restaurant,cuisine_type):
        self.resatrurant=restaurant
        self.cuisine_ytpe=cuisine_type
        self.number_servd=0
        #调用冰淇淋服务站信息方法
    def describe_restanurant( self ):
        res_name='冰淇淋服务站信息：'+self.resatrurant+self.cuisine_ytpe
        return  res_name
    #调用该方法 告诉客户 在营业
    def open_restaurant( self ):
        print('服务站正在营业')
        #统计卖了多少数量
    def restaurant_t( self ):
        if self.number_servd==0:
            print('还没有开张')
        else:
            print("今天卖了："+str(self.number_servd)+'个冰淇淋')
        #修改卖的数量
    def set_number_served( self ,number_servds):
        self.number_servd=number_servds
        #新增的数量(递增)
    def increment_number_served( self,miels):
        self.number_servd +=miels
        #创建一个子类，添加一个属性，已列表的方式存储 ，冰淇淋的口味
class IceCreamStand(Restaurant):
    #初始化父类的属性
    def __init__(self,restaurant,cuisine_type):
       super().__init__(restaurant,cuisine_type)
        #创建一个存储冰淇淋口味的方法
    def Taste( self,flavors ):
        self.flavors=flavors
       
#创建调用实例
restaurnt_y=Restaurant('爱蝶冰淇淋服务站','饮料冰淇淋专卖')
res_y=IceCreamStand('dweq','ewws')
print(res_y.describe_restanurant())
print(restaurnt_y.describe_restanurant())
res_y.Taste='8009'
print(res_y.Taste)
# restaurnt_y.resatrurant(8000)
restaurnt_y.restaurant_t()
restaurnt_y.open_restaurant()
restaurnt_y.restaurant_t()
restaurnt_y.set_number_served(800)#修改冰淇淋数量实例
restaurnt_y.restaurant_t()
restaurnt_y.increment_number_served(500)#新增数量实例
restaurnt_y.restaurant_t()

#
# class IceCreamStand:
#     #初始化类属性
#     def __init__(self,):

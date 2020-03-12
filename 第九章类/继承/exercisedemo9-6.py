'''''创建一个冰淇淋服务站'''
class Restaurant():
    #初始化类属性
    def __init__(self,restaurant,cuisine_type):
        self.resatrurant=restaurant
        self.cuisine_ytpe=cuisine_type
        self.number_serverd=0
        #调用冰淇淋服务站信息方法
    def describe_restanurant( self ):
        res_name='冰淇淋服务站信息：'+self.resatrurant+self.cuisine_ytpe
        return  res_name
    def open_restaurant( self ):
        print('服务站正在营业')
    def restaurant_t( self ):
        print("今天卖了："+str(self.resatrurant)+'个冰淇淋')
#创建调用实例
restaurnt_y=Restaurant('爱蝶冰淇淋服务站','饮料冰淇淋专卖')
print(restaurnt_y.describe_restanurant())
restaurnt_y.resatrurant=50
restaurnt_y.open_restaurant()
restaurnt_y.restaurant_t()
#
# class IceCreamStand:
#     #初始化类属性
#     def __init__(self,):

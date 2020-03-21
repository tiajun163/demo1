'''''在是第九章类的练习'''
#优化餐馆，新增就餐人数属性
#9-1餐馆
class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        ''''初始化类的属性'''
        self.restaurant_name=restaurant_name#餐馆名字
        self.restaurant_type=restaurant_type#餐馆类型
        self.number_serverd=0#设置默认的参数属性，默认为0
    #该方法调用餐馆的类型和名字
    def describe_restaurant( self ):
        name='什么类型的:'+self.restaurant_type+'店名是：'+self.restaurant_name
             
        return name #返回赋值的变量
    #该方法调用显示餐馆是在营业的
    def open_restaurat( self ):
        print(self.restaurant_name+'正在营业！'+'当前就餐人数:'+str(self.number_serverd))
    #该方法是调用修改的就餐人数
    def set_number_served( self,number_served ):
        self.number_serverd=number_served
    #该方法是调用递增的就餐人数
    def increment_number( self,number_serveds ):
    #加个判定条件，如果就餐人数大于5000了那就提示餐馆没有位置了
     if self.number_serverd>5000:
         print('餐馆已经没有位置了！')
     else:
         self.number_serverd +=number_serveds
#创建调用餐馆的实例
res=Restaurant('中华小厨神','中餐馆')
print(res.describe_restaurant())
#显示餐馆正在营业
res.open_restaurat()
#创建第二个实例
ueste=Restaurant('深夜食堂','综合饭馆')
ueste.describe_restaurant()
ueste.number_serverd=300
print(ueste.describe_restaurant())
ueste.set_number_served(100)
ueste.open_restaurat()
ueste.increment_number(1001)
ueste.open_restaurat()
#继承Restaurant类
class IceCeamstand(Restaurant):
    def __init__(self,restaurant_name ,restaurant_type='湘菜'):
        super().__init__(restaurant_name,restaurant_type)#初始化父类属性
        self.flavors=[]#初始化属性创建空列表
   #该方法调用的 是客人喜欢的口味
    def ice_res( self ):
      
        for flavors in self.flavors:
            print ("客人喜欢的口味："+flavors)
#创建实例
rs=IceCeamstand('小炒肉')
rs.flavors=['特辣','微辣','中辣']
print(rs.describe_restaurant())
rs.ice_res()
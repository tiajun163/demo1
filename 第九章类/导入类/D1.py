'''''在是第九章类的练习'''
#9-1餐馆
class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        ''''初始化类的属性'''
        self.restaurant_name=restaurant_name#餐馆名字
        self.restaurant_type=restaurant_type#餐馆类型
    #该方法调用餐馆的类型和名字
    def describe_restaurant( self ):
        name='什么类型的:'+self.restaurant_type+'店名是：'+self.restaurant_name
        return name #返回赋值的变量
    #该方法调用显示餐馆是在营业的
    def open_restaurat( self ):
        print(self.restaurant_name+'正在营业！')
#创建调用餐馆的实例
res=Restaurant('中华小厨神','中餐馆')
print(res.describe_restaurant())
#显示餐馆正在营业
res.open_restaurat()
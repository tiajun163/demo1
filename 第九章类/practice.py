''''练习9-1'''
class Restaurant():
    def __init__(self,res_name,cuis_type):
        #初始化属性
        self.res_name=res_name
        self.cuis_name=cuis_type
    def des_res( self ):
     print('des_res方法：调用'+self.res_name)
    def open_res( self ):
        print('open_res方法调用：'+self.cuis_name)

res=Restaurant('长沙','火车站')
print(res.cuis_name.title())
# print(res.des_res())
res.des_res()
''''9.2.1'''
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.module=model
        self.year=year
    def get_des( self ):
        #返回描述的信息
        long_name=self.year+':'+self.make+'!'+self.module+'....'
        return long_name
my_name=Car('audi','a5','2019')
print(my_name.get_des())
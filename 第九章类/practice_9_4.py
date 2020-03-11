'''''创建一个餐馆类'''
class Restauarant():
    def __init__(self,restuarant_name,cuisine_type):
        #初始化属性
        self.restuarnt=restuarant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    #返回餐馆信息
    def des_res( self ):
        user_ls="餐馆名："+self.restuarnt+'什么类型餐馆'\
                +self.cuisine_type+str(self.number_served)+'个人就餐'
        return  user_ls
    #修改就餐人数
    def set_number_served(self,served):
        self.number_served=served
    #新增就餐人数
    def increment_number_served(self,serveds):
        self.number_served +=serveds
rem_user=Restauarant('龙的传人','中餐')
rem_user.set_number_served(30)#就餐人数
rem_user.increment_number_served(9000)#添加就餐人数
print(rem_user.des_res())#打印出

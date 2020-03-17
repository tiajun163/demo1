'''''在是第九章类的练习'''
#9-5用户登录
class User():
    #初始化类属性
    def __init__(self,first_name,last_name):
        self.first_name=first_name#首次登录的用户名
        self.last_name=last_name#最近登录的用户名
        self.number_loin=0#登录次数
    #这个是调用首次登录和最近登录用户的方法
    def describe_user( self ):
        user_name=self.last_name+'是最近登录的用户\n'+\
                  self.first_name+'是首次登录的用户'+'登录了'+\
        str(self.number_loin)+'次'
        return user_name
    #这个是调用问候登录用户的方法
    def greet_user( self ):
        print("欢迎你："+self.last_name+'再次登录本系统')
        print('欢迎你：'+self.first_name+'首次登录本系统')
    #这个是调用新增登录次数的方法
    def install_login( self ):
        self.number_loin +=1
    #这个是如果登录次数为1，者清空为0
    def rest_login( self ):
        self.number_loin=0
        
#创建调用用户实例
users=User('小蝶','老田')
print(users.describe_user())
users.greet_user()
#登录实例
users.install_login()
users.install_login()
users.install_login()
users.install_login()
users.install_login()
print(users.number_loin)
#调用清零方法
users.rest_login()
userst=User('arl','竹')
print(userst.describe_user())
userst.greet_user()

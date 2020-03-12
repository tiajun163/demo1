class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
        #返回信息
    def describe_user( self ):
        user=self.first_name+'你好'+self.last_name+'上次登录次数'+\
             str(self.login_attempts)
        return  user
    #打印问候
    def greet_user(self):
        print("欢迎你们")
        #添加登录次数
    def increment_login_attempts( self,attemt ):
        self.login_attempts +=attemt
        #重置次数
    def reset_login_attempts( self ):
        if self.login_attempts>1:
            self.login_attempts=0
        else:
            print('没有登录过')
users=User('ALR','。。。。')
print(users.describe_user())
users.greet_user()
users.increment_login_attempts(0)
print(users.describe_user())
users.reset_login_attempts()
print(users.describe_user())
users.reset_login_attempts()

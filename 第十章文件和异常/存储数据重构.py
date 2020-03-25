import  json
#重构
def gree_user():
    """如果用户存储了用户，就获取他"""
    filename='username2.json'
    #异常处理
    try:
        #读取文件
        with open(filename)as f:
            #使用load（）方法读取文件内容
            username=json.load(f)
    #抛出异常
    except FileNotFoundError:
        #返回None
        return  None
    else:
        #返回有切返回用户名字
        return  username
def get_user():
    """问候用户，并指出名字"""
    username=gree_user()
    #if条件判断是否存在文件并打印出名字
    if username:
        print('你的名字已登记'+username)
    else:
        #如果文件不存在，创建文件 存储 用户输入的名字
        username=input("请输入你的名字：\n")
        filename='username2.json'
        #创建文件写入模式
        with open(filename,'w')as f:
            #使用dump()方法存储数据
            json.dump(username,f)
            print('已保存你的名字：'+username)
#调用函数
get_user()
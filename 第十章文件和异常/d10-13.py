import  json
#练习10-13验证用户
#获取的已有的用户名
def get_stored_user():
    fienname='username.json'
    try:
        with open(fienname)as f:
           uanme= json.load(f)
    except FileNotFoundError:
        return  None
    else:
        return  uanme
#输入用户名 并存储到文件中
def get_new_username():
    con=input("输入你的姓名：\n")
    fien='username.json'
    with open(fien,'w')as f:
        json.dump(con,f)
        
    return con
#调用问候语
def greet_user():
    usernames=get_stored_user()
    if usernames:
        cour=input("你是存在：{usernames}？（y/n)")
        if cour=="y":
            print()
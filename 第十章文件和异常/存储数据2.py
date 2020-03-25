import  json
fiename='username1.json'
try:
    with open(fiename)as f1:
        con= json.load(f1)
except FileNotFoundError:
    username=input('请输入你的名字：\n')
    with open(fiename,'w',encoding='utf-8')as f:
        json.dump(username,f)
        print('你输入的名字记录：'+username)
else:
    print('你回来了：'+con)
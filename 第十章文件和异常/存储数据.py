import json

# 使用函数dump()存储数据
num1 = [ 1, 2, 3, 4, 5, 7, 1 ]
fiename = 'num1.json'  # 将列表数据存储到指定的文件中去
with open (fiename, 'w')as f:  # 将列表数据写入到json文件中去
    json.dump (num1, f)  # 使用函数dump()将数据存储到num1.json文件中去

# 使用函数load()读取
fienmaes = 'num1.json'
# 读取文件
with open (fienmaes)as f1:
    # 将文件加载出来使用load()函数
    nums = json.load (f1)
print (nums)

# -----保存和读取用户生成的数据----
#存储用户输入的名字
uname=input('请输入名字：\n')
fname='username.json'
with open(fname,'w')as fn:
    json.dump(uname,fn)
    print('你回来了:'+uname)
#读取用户存储的数据
fname1='username.json'
with open(fname1)as fns:
    us=json.load(fns)#读取存储的数据
    print('记录的名字：'+us)

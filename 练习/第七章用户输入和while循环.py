# #input函数
# # test=input()
# # print(test)
# #使用int()方法获取数值输入
# # print(input(int))
# age=input()
# age=int()
# # age=input()
# print(age>20)
# nuber=input()
# nuber=int(nuber)
# if nuber %2==0:
#     print(str(nuber)+'是偶数')
# else:
#     print(str(nuber)+'是奇数')
#
# uname=input('你好需要什么汽车：')
# print('你需要的'+uname+'暂时没有')
# test=input("请问几个人用餐")
# test=int(test)
# if test>8:
#     print("不好意思没有位置")
# else:
#     print('欢迎光临这边请')
# unmwhile=1
# # unmwhile=int()
# while unmwhile<=5:
#     print('输入',unmwhile)
#     unmwhile+=1
# prompt='请输入，如需要退出输入 quit'
# message=''
# while message!='quit':
#     message=input(prompt)
#     print(message)
# """""'''''''''''"""
# fals='你哈啊  '
# fal=True#设置变量为True
# while fal:
#     message=input(fals)#使用input()函数 ，输入fal变量值
#     if message=='qiut':#判断输入的字符是否等于qiut
#         fal=False
#     else:
#         print(message)
# ''''使用brenk结束while循环'''
# prmpt="请输入内容，如需退出输入quit！"
# while True:
#     city=input(prmpt)
#     if city=='quit':
#         break
#     else:
#         print('我喜欢你：'+city.title()+'!')
# ''''''''
# current_number=-2#定义一个变量
# while current_number<10:
#     current_number +=1 #current_number+1
#     if current_number % 2==0:
#         continue
#     print(current_number)#打印出
# '''''练习'''
# test='请输入披萨坯料，如需退出输入quit'
# while True:
#     number=input(test)
#     if number=='quit':
#         break
#     print('你要的披萨添加了'+number.title()+"配料")
# age=input("请问是要买电影票吗？需要告诉下我你的年龄")
# age=int(age)
# if age>3:
#     print('你好你的票价是10元')
# elif age>12:
#     print('你好你的票价是15元')
# else :
#     print('小可爱你免费额')
#创建一个待验证的用户列表
# uncofirmed_users=['alice','brian','candace']
# #创建一个存储已验证的用户的空列表
# cuncofirmed_user=[]
# #验证每个用户，直到没有尾验证的用户
# #将每个验证的用户存储到已经验证的用户列表
# while uncofirmed_users:
#     uncofirmed_userl=uncofirmed_users.pop()
#     print("打印出"+uncofirmed_userl.title())
#     cuncofirmed_user.append(uncofirmed_userl)
# print("显示已验证用户")
# for cuncofirmed_user in cuncofirmed_user:
#     print("已验证用户"+cuncofirmed_user.title())
# #删除包含特定值的所有列表元素
# #创建一个列表
# pest=['dog','cat','dog','xiaodie','goldfish','cat','rabbit','cat']
# print(pest)#打印列表
# while 'cat' in pest:#循环判断是否还有元素cat
#     pest.remove('cat')#删除掉cat元素
# print(pest)#打印删除之后的列表元素
# #创建一个空字典
# responses={}
# #设置一个标志，指出调查是否继续
# poling_active=True
# while poling_active:
#     name=input('输入调查者的名字和回答')
#     response=input("调查者的回答：")
#     responses[name]=response#将答案存储到字典中
#     #查看是否还有人要参与调查
#     repeat=input("还有人需要参与调查吗？不需要输入no：")
#     if repeat=='no':
#         poling_active=False
# print('调查结果如下')
# #遍历字典，打印出字典的键和元素
# for name ,response in responses.items():
#     print(name+':'+'的答案是：'+response)
# #打印出字典
# print(responses)
#三明治
sandwich_orders=['nr','bc','ml','pastrami','pastrami','pastrami']#c创建列表包含3个元素
sandich=[]#创建一个空列表

while sandwich_orders:
    stest=sandwich_orders.pop()#每次删除掉列表最后一个值，赋值给stest
    print("三明治："+stest.title())
    sandich.append(stest)#把值添加到列表中
print(sandich)#打印列表
for sandich in sandich:#遍历列表输出元素
    print("我要这个三明治;"+sandich.title())

# """"
# 1、将一些朋友的姓名存储在一个列表中，并将其命名为names。
# 依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
# 2、继续使用练习1中的列表，但不打印每个朋友的姓名，
# 而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名
#
# 3、想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表
# 。根据该列表打印一系列有关这些通勤方式的宣言
# """
# names=['田俊','小蝶','Arl','大A','垃圾袋']
# "无脑打印出来"
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# #二进制
# a2=0b111000011001
# print(a2)
# #2
# print(names[0]+':您好！')
# print(names[1]+':好久不见')
# print(names[2]+":hello")
# print(names[3]+':我是你大爷')
# print(names[4]+':你妹')
# #3
# vehicle=['火车','汽车','游轮','飞机']
# ''''
# 3-4 嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的）
# ，你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；
# 然后，使用 这个列表打印消息，邀请这些人来与你共进晚餐。
# 3-5 修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，
# 因此需要另外邀请一位嘉宾。 以完成练习3-4时编写的程序为基础，
# 在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。 修改嘉宾名单，
# 将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。 再次打印一系列消息，
# 向名单中的每位嘉宾发出邀请。
# 3-6 添加嘉宾 ：你刚找到了一个更大的餐桌，
# 可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，
# 指出你找到了一个更大的餐桌。 使用insert() 将一位新嘉宾添加到名单开头。
# 使用insert() 将另一位新嘉宾添加到名单中间。
# 使用append() 将最后一位新嘉宾添加到名单末尾。 打印一系列消息，
# 向名单中的每位嘉宾发出邀请。
# 3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，
# 因此只能邀请两位嘉宾。 以完成练习3-6时编写的程序为基础，
# 在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
# 每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，
# 无法邀请他来共进 晚餐。 对于余下的两位嘉宾中的每一位，都打印一条消息，
# 指出他依然在受邀人之列。 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。
# 打印该名单，核实程序结束时名单确实是空的。
# '''
# #1
# guestReception=['小李','小吴','小蝶','小王','小小']
# # for i in guestReception:
# #     for i in 4:
# #         i=0
# #         print('周五聚会'+guestReception[i])
#
# #小李无法到
# del guestReception[0]
# print(guestReception)#打印出列表
# #要求小王
# guestReception[0]='小王'
# print(guestReception)#打印列表
# #在邀请3位
# guestReception.insert(0,'xx')
# guestReception.append('爱你吆')
# guestReception.insert(4,'aaaaa')
# print(guestReception)
# #只能邀请2位其他劝退
# guestReception.pop()
# print(guestReception)
# guestReception.pop(0)
# print(guestReception)
# print(guestReception)
# a='python'
# b='python 1'
# print(a==b)
# print(b.rstrip())
# print(id(b))
# #转换类型
# c=123
# c=str(c)
# print(type(c))
# print(c)
NAME ='arl'
print(NAME+':hello eric,would you like to')
print(NAME.lower())#全部小写
print(NAME.title())#首字母大写
print(NAME.upper())#全部大写
print("hhs::\ttyy\nlos\ttyy2\nsdd")
#创建一个列表
bicycle=['arl','小蝶','love']
bicycle1=['a','c','d','h','f']
print(bicycle[0])
bicycle.append('hello')
print(bicycle)
bicycle.insert(1,'you')
print(bicycle)
bicycle.remove('you')
print(bicycle)
bicycle.sort()#使用sort方法排序列表
print(bicycle)
bicycle.sort(reverse=True)
print(bicycle)
print(sorted(bicycle))#使用sorted函数临时排序
bicycle.reverse()#倒序排列
print(bicycle)
print(len(bicycle))#判断列表长度
landscape=['泰山','西藏','华山','云南大理','长白山']
print(sorted(landscape))
print(landscape)
print(sorted(landscape))
print(sorted(landscape,reverse=True))
print(landscape)
landscape.sort()
print(landscape)
print(len(landscape))
print(landscape[1])
'''遍历列表'''''
for landscape in landscape :
    print(landscape)
for bicycle in bicycle:
    print(bicycle.title()+"：您好！")
    print('早点来上班！别迟到，'+bicycle.rstrip()+'.\n')
for bicycle in range(1,6):
    print(bicycle)
#创建数字列表
numbers=list(range(0,10))
print(numbers)
numbers1=list(range(0,15,3))#每次加3
print(numbers1)
#创建空列表
numbers2=[]
for list1 in range(1,10):
    numbers=list1**2
    numbers2.append(numbers)
    print(numbers2)
numbers2=[]
for list1 in range(1,5):
    numbers2.append(list1**2)
    print(numbers2,"\t")
    print(min(numbers2))#打印最小值
    print(max(numbers2))#打印最大值
    print(sum(numbers2))#求和


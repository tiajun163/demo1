'''使用for循环打印1-20包含数字'''
for list in range(1,21):
    print(list)
''''创建一个列表 包含1-10000000，并使用for循环打印出来'''
list=[]
for list1 in range(1,10):
    list.append(list1)
    print(list)
    print(sum(list))
list=[list1 for list1 in range(1,20,2)]
print(list)
for list in list:
    print(list)
list=[list**3 for list in range(1,11)]
print(list)
print(list[0:3])
for list in list:
    print(list)
''''切片'''
list=['arll','小蝶','老莫','老尹','老严',]
print(list[0:3])
print(list[2:-1])
print(list[-3:])
# #遍历切片元素
# for list in list[0:3]:
#     print(list.title())#首字母大写
listt=list[:]
print(listt)
listt.append('hello1')
print(listt)
print(list)
# for list in list[0:3]:
#     print('hello !你好！'+list)
for list in list[0:2]:
    print('欢迎你'+list)
print(list)
''''元组'''
#创建元组
dimension=(200,500,600,700)
print(dimension)
for dimension in dimension:
    print(dimension)
dimension1=(1,2,3,4,5,6,7)
# dimension1[0]=300
print('没修改\t：')
print(dimension1)
#修改元组变量
dimension1=(10,11,12,13,14)
print('修改之后：')
print(dimension1)
for dimension1 in dimension1:
    print(dimension1)

"""

创建一个简单列表 并输出
"""
bicycle=['love','I','12','yes']
print(bicycle)
print(bicycle[0])#通过索引位置  访问列表元素
print(bicycle[0].title())
'''
修改列表元素
'''
bicycle[0]='Areng'
print(bicycle)
bicycle1=[]#创建一个空列表,使用apped方法 添加元素
bicycle1.append('love')
bicycle1.append('阿瑟表示')
bicycle1.append('还有个的肝')
print(bicycle1)#打印列表元素
del bicycle1[1]#删除列表元素
print(bicycle1)
print(bicycle)
#使用pop方法删除元素,pop删除最后一个元素
bicycleTest=bicycle.pop()
print(bicycle)
print(bicycleTest)
bicycle.remove('I')#remove方法删除指定的元素值
print(bicycle)
#help(str)
print(bicycle)
# import  keyword #引入关键字模块
# print(keyword.kwlist)#打印出系统全部的关键字

motycles=[]
motycles.append('你好')
motycles.append('love')
print(motycles)
namel=input()#输入添加的元素
motycles.append(namel)
print(motycles)
names=input()
motycles.remove(names)#删除元素
'''
pop方法删除最后一个元素，但是  还是可以继续使用，del方法删除元素之后不在使用
remove方法删除指定元素，
'''
print(motycles)

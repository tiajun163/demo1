'''''第一个试例'''
#创建一个列表
cars=['大A','老莫','老尹','a小蝶','arl']
for cae in cars:
    if cae=='a小蝶':
        print(cae.title())#如果有小蝶就首字母大写
    else:
        print(cae.upper())#如果没有小蝶就全部大写
car='a'
print(car=='a')
print(car=='b')
TestDemo=['lan','len','alr','test','lower']
# for abc in TestDemo:
#     if abc=='len'or abc=='alr':
#         print(abc.title())
#         print(True)
#     else :
#         print(abc.upper()
# #               )
# #         print(False)
# test1='a'
# test2='a'
# test1==test2
print("判断是否包含：",'lan' in TestDemo)
print("判断是否不包含",'alr'not in TestDemo)
alien_color=['green','yellow','red']
if 'green' in alien_color:
    print("获得5点")
else:
    print('获得10点')
if 'green3' in alien_color:
    print("555")
elif 'yellow' in alien_color:
    print('666')
else:
    print('000')
age=64.5
if age<2:
    print('婴儿')
elif age<4:
    print('小孩')
elif age<13:
    print('儿童')
elif age<20:
    print('少年')
elif age<65:
    print('成年人')
# elif age>=65:
#     print('老年人')
else:
    print('老年人')
#多个列表使用if
Demo1=['A','B','C','D']
Demo2=['a','b','c','d']
for demo in Demo1:
    if demo.lower() in Demo2:
        print('满足')
        # print(sorted())
    else:
        print('不满足')
        print(Demo2)
#练习
#1、创建 一个列表包含5个用户名，每次登陆 打印一句话
TestDemo=['小蝶','旺旺','arl','小吴','love','admin']
for test in TestDemo:
    print(test+':\n'+'hello,您好！')
#如果用户名是admin就打印一句 你迟到了，并且全部大写
TestDemo1=['小蝶','旺旺','arl','小吴','love','admin']
for test in TestDemo:
 if test=='admin':
    print(test.upper(),':\t'+'你迟到了')
 else:
     print(test+'::\t'+'你好')
#判断列表是否为空
a=[]
if len(a)>0:
    print(True)
else:
    print(False)
TestDemo1=['小蝶','旺旺','arl','小吴','love','admin']
#判断 列表是否为空 ，如果为空，就打印 你大爷
if len(TestDemo1)<0:
    print('你大爷')
else:
    print('你二爷')
    # print(TestDemo1.pop())
    # print(TestDemo1)
#判断列表 是否为空，如果不是空列表，删除元素 一直到为空 打印出 你好终于为空了
TestDemo1=['小蝶','旺旺','arl','小吴','love','admin']
if len(TestDemo1)>0:
    test=len(TestDemo1)-1
    print(TestDemo1.pop(test))
    print('减掉第'+'列表元素')
    # print(test)
else:
    print('你终于空了')

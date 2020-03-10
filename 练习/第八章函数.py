# def test(name_l):
#     print('早上好'+name_l.title())
# test('xiaode')
# def favorite_book(titles):
#     print('你要的书名：'+titles.title())
# favorite_book(input("请输入你的书名："))
# # #传多个参数
# def fbook(name,price):
#     print(name.title()+'书名')
#     print(price+'价格')
# fbook('yj','25')
# fbook('ss','89')
# fbook(input('请输入书名'),input('输入价格'))
# # #关键字实参
# def describe_pet(animal_type,pet_name):
#     print("动物类型;"+animal_type)
#     print("动物名字"+pet_name.title())
# describe_pet(animal_type='猫',pet_name='jik')
# # #创建函数且定义一个默认值
# def tes(tyoe,name='dog'):
#     print('你二大爷是：'+name)
#     print('你三大爷是：'+tyoe)
# tes('无敌风火轮')
# tes(tyoe='哪吒',name='无敌风火轮1')
# # #练习
# def make_shrit(size,words):
#     print('尺寸大小 ：'+size)
#     print('留言：'+words.title())
# make_shrit(size='50',words='愿你归来任少年')
# # #练习2
# def make_city(name="中国",cityname='南昌'):
#     print("城市名;"+cityname)
#     print("属于国家"+name)
# make_city('美国','纽约')#传实参
# make_city()#使用默认值
# make_city('zg','深圳')
# ''''返回值'''
# def get_name(firs_name,last_name):
#     #定义一个变量
#     fuLll_name=firs_name+"我是你"+last_name+'的大爷'
#     return fuLll_name.title()
# testname=get_name('wud','jm')#返回值赋值给变量
# print(testname)
# #使用条件判断是否传默认值
# def get_name1(firs_name,last_name,test_name=''):
#     #定义一个变量
#     if test_name:
#
#        fuLll_name=firs_name+"我是你"+last_name+'的大爷'+test_name
#     else:
#         fuLll_name=firs_name+'你大爷是你'+last_name+'的老爸'
#     return fuLll_name.title()
# testname=get_name1('wud','jm','啊啊啊')#返回值赋值给变量
# print(testname)
# #返回字典
# def build_person(first_name,last_name):
#     """返回一个字典，包含一个人的信息"""
#     person={'first':first_name,'last':last_name}
#     return person
# mis=build_person('jiml','hek')#传值
# print(mis)
# #使用条件判断形参 函数传值
#
# def build_person1(first_name,last_name,age=''):
#     """返回一个字典，包含一个人的信息"""
#     person={'first':first_name,'last':last_name}
#     if age:
#         person['age']=age
#     return person
# mis=build_person1('jiml','hek','27')#传值
# print(mis)
# #使用函数和while循环
# def  get_formatted_name(first_name,last_name):
#     full_name=first_name+'喜欢'+last_name
#     return  full_name.title()
# while True:#判断是否要退出
#     print('输入喜欢你的名字')
#     print('退出输入q')
#     f_name=input("请输入名字")
#     if f_name=='q':
#         break
#     l_name=input('请输入下一个名字')
#     if l_name=='q':
#         break
# form_name=get_formatted_name(f_name,l_name)
# print(form_name)
# #练习8-6
# def city_country(city_name,state_name):
#     full_name='"'+city_name+','+state_name+'"'
#     return full_name.title()
# tename=city_country('cs','zg')
# print(tename)
#
#
# ##练习8-7
# def make_album(Tname,L_name,number=''):
#     makeps={'singer':Tname,'name':L_name}
#     if number:
#         makeps['number']=number
#     return makeps
# mis=make_album('许嵩','有何不可','100w')
# print(mis)
# mis=make_album('周杰伦','听妈妈的话','1000w')
# print(mis)
# '''''传递列表'''
def gre_list(unames):#创建函数
    for name in unames:#遍历列表元素
        msg="早上好："+name.title()#创建变量
        print(msg)#打印
usernames=['小蝶','无敌风火轮','Arl','老田']
gre_list(usernames)
''''函数中修改列表'''
#创建一个列表
'''使用while循环处理'''
list1=['xiaodie','wd','resid','hello','Alr','goobbook']
#创建一个空列表
list2=[]
while list1:
    listT=list1.pop()#每次删除列表最后一个元素赋值给变量listT
    print(listT+'lisT值')#
    list2.append(listT)#每次从列表最后添加一个元素listT
    print(list2,'列表元素')
for listname in list2: #遍历list2列表
    print(listname.title())#打印出列表元素
print(list2)
''''修改上面的使用函数处理'''
def list_print(list_1,list_2):#这个函数处理把一个列表元素提取到另一个列表去
    '''创建函数 传2个参数'''
    while list_1 :
        list_del=list_1.pop()#每次删除列表元素最后一个值
        print('打印出列表元素;'+list_del)
        list_2.append(list_del)#每次列表都添加一个元素
        print(list_2,'list_2列表元素')
def list_append(list_2):
    for list_name in list_2:#遍历列表元素打印出来
        print(list_name.title())
list_1=['xiaodie','wd','resid','hello','Alr','goobbook']
list_2=[]
list_print(list_1,list_2)#传实参
list_append(list_2)
# print('函数',list_append(list_2='小蝶'))
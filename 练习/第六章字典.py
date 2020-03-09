alien_0={'clor':'ls','yello':'dw'}#创建一个字典
print(alien_0['clor'])#打印访问字典
print(type(alien_0))#打印变量是什么类型
# print(alien_0)
alien_0[1]=2#添加键值
alien_0['print']='love'
print(alien_0)
#修改字典中的值
alien_0={'alr':0,'小蝶':'ai','test':'love'}
#使用if判断然后修改字典中的值
if alien_0['test']=='love1':
    alien_0['alr']=2
    alien_1=2
elif alien_0['test']=='false':
    alien_1=3
    alien_0['alr']==3
else:
    alien_1=5
    alien_0['alr']=5
    alien_0['alr']=alien_0['alr']+alien_1
    print(str(alien_0['alr']))
print(alien_0)
#删除键值对,使用del删除 永久删除
del alien_0['alr']
print(alien_0)
#练习1；使用字典存储熟人，年龄，姓名，城市，居住城市
dict_1={'age':'26',
        'name':'小蝶',
        'cs':'长沙',
        'jy':'岳阳'}
print(dict_1)
#遍历字典
for k,T in dict_1.items():
    print('\nk:'+k)
    print('T:'+T)
dict_2={'age':'26',
        'name':'小蝶',
        'cs':'长沙',
        'jy':'岳阳'}
friends=['age','name']#创建一个列表，然后判断
#使用keys()方法遍历所有字典中的键
for name in dict_2.keys():#遍历出字典中所有的键
    print(name)
    if name in friends:#遍历出键对应的值
        print('hello你好！'+name.title()+'!'+dict_2[name].title())#打印出对应的字典键值
#使用sortend()方法按顺序遍历字典中的值
ict_2={'age':'26',
        'name':'小蝶',
        'cs':'长沙',
        'jy':'岳阳',
       'ages':'26'}
for name in sorted(ict_2.keys()):
    print(name.title()+'啊啊啊')
#使用values()方法遍历字典中所有值
for name in ict_2.values():
    print(name.title()+'字典所有值')
#使用set（）方法去掉重复值
for name in set(ict_2.values()):
    print('\t\n'+name+'去掉重复值')
#练习
#创建字典
test={
    'c':'c-',
    'c++':'c+',
    'java':'java+',
    'python':'python+',
    'js':'js+',
    'roeds':'roeds=',
    'php':'php+',
    'mysql':'mysql+'
}
#使用items()方法遍历
for key,name in test.items():
    print(key+'='+name)
    # print(key)
    # print(name)
test1=['c','java','c++','python','js','mysql','php','roeds']
for name  in  sorted(test.keys()):#按顺序遍历所有键
    print('遍历字典键：'+name)
    if name in test1:#键对应的值
        print(name.title()+'键对应的值是：'+test[name].title())
#嵌套字典
t1={'a':'a','b':'B'}
t2={'c':'C','d':'D'}
t3={'e':'E','f':'F'}
testDemo=[t1,t2,t3]
for testDemo1 in testDemo:
    print(testDemo1)
list1=[]#创建空列表
for alien in range(30):
    list={'alr':'gren','all':'grso','points':5}
    list1.append(list)
    # print(list1)
    for alien_0 in list1[:5]:
        print(list)
print(len(list1))
#字典中嵌套列表
dict={'name':'小蝶','age':['10','20','30','40','50','60','70','80','90','100','110','120']}
# print(dict)
for name ,age in dict.items():
    print(name)
    for ages in age:
        print(ages.title())
#创建一个字典嵌套字典
dict1={
    'test':{
        'python':'python1',
        'java':'java1'
    },
    'demo':{
        'python':'C1',
        'java':'JS1'
    },
    'HELLO':{
        'python':'php1',
        'java':'mysql'
    }
}
print('----------------------------------')
'''
内部字典键值名一样，但是值是不一样
'''
for name,key in dict1.items():#遍历字典
    print('键：'+name)#打印遍历出的键.且首字母大写
    test_key=key['python']+key['java']
    # demo_key=key['C']+key['JS']
    # HELLO_key=key['php']+key['mysql']
    print('Test键对应的值：'+test_key.title())
    # print('demo对应的值：'+demo_key.title())
    # print('HELLO键对应的值：'+HELLO_key.title())
#练习
#列表包含字典
# list_demo=[]
list_dict={'name':'alr'}
list_dicts={'name ':'xiaodie'}
# list_demo=list_dict+list_dicts
list_demo=[list_dicts,list_dicts]
# print(list_demo)#打印列表
for name  in list_demo:#遍历列表
    print(name )#打印列表
pets=[]
for name in range(5):
    Pets_name={'name':'zhandie','age':5}
    pets.append(Pets_name)

    print(pets
          )
    #创建一个字典，人名 对应喜欢的地方
favorite_placse={
    'arl':['深圳','长沙','南昌'],
    'xiaodie':['长沙','岳阳','汨罗'],
    'aren':['南昌','北京','纽约']
}
# print(favorite_placse.items())
for name ,love in favorite_placse.items():
    print(name.title())#打印每个人名并首字母大写
    for loves in love:
        print(loves.title())#打印出每个人喜欢的地方
#创建一个字典citites 并将3个城市做完键
citites={'长沙':{
    'country':'中国',
    'pupolation':'2000w',
    'fact':'cs'
},
    '纽约':{
        'country': '美国',
        'pupolation': '5000w',
        'fact': 'ny'
    } ,
    '伦敦':{
        'country': '英国',
        'pupolation': '4000w',
        'fact': 'ld'
    },
}
for name ,keytest in citites.items():
    print('城市名：',name)#打印健名
    print('属于哪个国家：',keytest['country'])
    print('该城市人口多少：',keytest['pupolation'])
    print('id多少：',keytest['fact'])

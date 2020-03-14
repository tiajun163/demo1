from collections import OrderedDict
from  random import  randint
faca = OrderedDict ()
faca [ 'diexiao' ] = 'arl'
faca [ 'wd' ] = 'ewq'
faca [ 'yute' ] = 'rew'

# 遍历字典
for name, lang in faca.items ():
    print (name.title () + '字典键对应的值=' + lang.title ())
    print (faca)
x=randint(1,6)
class Die():
    """""创建初始化方法类的属性"""
    def __init__(self,sids=6):
        self.sids=sids
    def roll_die( self ):#roll骰子
        return  randint(1,self.sids)
D6=Die()#创建实例
# print(D6.roll_die())
results=[]
for roll_num in range(10):#遍历
    result=D6.roll_die()
    results.append(result)#按列表递增（末尾新增）
    # print(result)
print("打印10卷六面模的数字：")
print(results)

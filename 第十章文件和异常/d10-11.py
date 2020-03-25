#练习10-11
import  json
number=input("输入你喜欢的数字：\n")
funber='numbers.json'
with open(funber,'w')as f:
        json.dump(number,f)
        print('你喜欢的数字是：\n'+number)
        
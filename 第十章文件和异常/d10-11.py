#练习10-11
import  json
# number=input("输入你喜欢的数字：\n")
funber='numbers.json'
# with open(funber,'w')as f:
#         json.dump(number,f)
#         print('你喜欢的数字是：\n'+number)
#练习10-12
try:
    with open(funber)as f:
        con=json.load(f)
except FileNotFoundError:
    number = input ("输入你喜欢的数字：\n")
    with open(funber,'w')as f:
        json.dump(funber,f)
        print('你登记的数字：'+number)
else:
    print(
        '你喜欢的数字已登记为：'+con
    )
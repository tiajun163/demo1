#练习数字加法
# try:
#     x=input('输入数字X:\n')
#     x=int(x)
#     y=input('输入数字Y:\n')
#     y=int(y)
# except ValueError:
#     print('不能输入其他字符，只能是数字')
# else:
#     sum=x+y
#     print('x+y的和为：'+str(sum))
#使用while循环
print('退出输入q')
while True:
    try:
        x=input('输入数字X:\n')
        if x=='q':
            break
        x=int(x)
        y=input('输入数字Y：\n')
        if y=='q':
            break
        y=int(y)
    except ValueError:
        print('不能输入字符，只能数字')
    else:
        sum=x+y
        print("x+y的和为："+str(sum))
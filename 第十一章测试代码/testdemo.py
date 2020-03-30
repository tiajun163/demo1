from 第十一章测试代码.test import get_name
print('退出请输入q')
while True:
    first=input("输入你的名字：\n")
    if first=='q':
        break
    last=input("输入你的姓名：\n")
    if last=='q':
        break
    full_names=get_name(first,last)
    print('合并之后的名字：'+full_names)
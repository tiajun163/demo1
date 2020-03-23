name='d.txt'
print('完成之后输入quit()退出')
while True:
    names=input("请输入你的名字：")
    if names=='quit()':
        break
    else:
        with open(name,'a')as n:
            n.write(names+'\n')
        print('Hi！'+names+'你的名字添加到了留言板上了')
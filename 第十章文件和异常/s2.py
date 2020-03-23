name='d.txt'#读取文件
print('完成之后输入quit()退出')
while True:#使用while循环
    names=input("请输入你的名字：")
    if names=='quit()':#if条件语句
        break
    else:
        with open(name,'a')as n:#读取文件
            n.write(names+'\n')#写入
        print('Hi！'+names+'你的名字添加到了留言板上了')
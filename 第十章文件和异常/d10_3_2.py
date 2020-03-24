#使用try-except处理异常，
try:
    print(5/0)
except ZeroDivisionError:
    print('除数不能为0')
#使用try-except-else处理异常
print('输入数字：')
print('退出输入q')
while True:
    finame=input('\n 输入数字:')
    if finame=='q':
        break
    sname=input('\n 输入除数:')
    if sname=='q':
        break
    try:
        ase=int(finame)/int(sname)
    except ZeroDivisionError:
        print('除数不能为0！')
    else:
        print(ase)
        
        
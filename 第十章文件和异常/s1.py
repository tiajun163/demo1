#练习10-3访客
name='s.txt'
with open(name,'r+') as file_obj:
    file_obj.write(input('请输入你的名字！'+'\n'))
names=input("请输入你的名字")
fiel='ss.txt'
with open(fiel,'a') as fie_obj:
    fie_obj.write(names+'\n')
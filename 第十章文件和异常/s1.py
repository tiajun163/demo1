#练习10-3访客
name='s.txt'
with open(name,'r+') as file_obj:
    file_obj.write(input('请输入你的名字！'))
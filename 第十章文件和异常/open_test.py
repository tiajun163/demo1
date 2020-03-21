# with open("E:\\工作\\脚本\\reuname.csv") as  file:
#     con=file.read()
#     # print(con.rstrip())
#     print(con)
#
# name="E:\\工作\\脚本\\reuname.csv"
# with open(name) as file_name:
#    for username in file_name:
#        # print(username.rstrip())#清除空格
#        print(username.rsplit())#已列表格式
#        print(username.strip())
#        print(username)
# '''''创建一个包含文件各行内容的列表'''
# name="E:\\工作\\脚本\\reuname.csv"
# with open(name) as file:
#     lins=file.readlines()
#     # print(lins)
#     for line in lins:
#          print(line.rstrip())
# pi_s=''
# for lis in lins :
#     pi_s +=lis
# print(pi_s)
# print(len(pi_s))
''''包含一个百万的大型文件'''
# filenname="demo.txt"
# with open(filenname) as fiel:#读取文件，打开文件路径
#     lin=fiel.readlines()#读取文件数据
# pi_st=''
# for line in lin:
#     pi_st+=line.strip()
# print(pi_st[:56]+'...')
# print(len(pi_st))
#读取相对路径的文件
# name='D:\\Python\\demo1\\第九章类\\t1.txt'
# with open('D:\\Python\\demo1\\第九章类\\t1.txt') as fiel:
#     lin=fiel.read()
#     print(lin)
'''''圆周率包含你的生日'''
name='demo.txt'
with open(name) as fiel_object:
    lin=fiel_object.readlines()
pi_staring=''
for lin_name in lin:
    pi_staring+=lin_name.rstrip()
bi=input("输入你的生日：")
if bi in pi_staring:
    print('包含了')
else:
    print('不包含')
    
    
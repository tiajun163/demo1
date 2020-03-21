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
filenname="demo.txt"
with open(filenname) as fiel:
    lin=fiel.readlines()
pi_st=''
for line in lin:
    pi_st+=line.strip()
print(pi_st[:56]+'...')
print(len(pi_st))
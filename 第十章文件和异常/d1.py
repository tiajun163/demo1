# #练习10-5
fiellname='d1.txt'
res=[]
while True:
    re=input('你喜欢编程的理由：\n')#输入
    res.append(re)#每次输入添加到列表后面
    con=input("你想其他人回应？(y/n)\n")
    if con!='y':
        break
with open(fiellname,'a')as f:
    for names in res:#遍历列表
        f.write(names+'\n')#写入文件
# filename = 'programming_poll.txt'
#
# responses = []
# while True:
#     response = input("\nWhy do you like programming? ")
#     responses.append(response)
#
#     continue_poll = input("Would you like to let someone else respond? (y/n) ")
#     if continue_poll != 'y':
#         break
#
# with open(filename, 'a') as f:
#     for response in responses:
#         f.write(f"{response}\n")
#处理找不到文件异常
# fian='xx.txt'
# with open(fian)as f:
#     cs=f.read()
#处理异常
# fian='xxx.txt'
# try:
#     with open(fian)as f:
#         mai=f.read()
# except FileNotFoundError:
#     ss='你查找的'+fian+'文件不存在'
#     print(ss)
#分析文本
fian='xs.txt'
try:
    with open(fian) as f:
        con=f.read()
except FileNotFoundError:
    msg='这本'+fian+'有多少字'
    print(msg)
else:
    #计算文件大致包含多少个字
    word=con.split()
    num=len(word)
    print('这本'+fian+'有'+str(num)+'字')
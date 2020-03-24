#使用函数处理多个文件
def count_words(filename):
    try:
        with open(filename) as f:
            con=f.read()#读取文件
    except FileNotFoundError:
        msg='该'+filename+'文件不存在'
        print(msg)
    else:
        words=con.split()#计算文件包含多少
        num=len(words)#
        print('这个'+filename+'文件包含'+str(num)+'字')
        
#创建实例
# filename='test.txt'
# count_words(filename)
#使用列表
filenames=['ss.txt','xs.txt','test.txt',
           'd.txt','d1.txt','demo.txt','s.txt']
for filename in filenames:
    count_words(filename)
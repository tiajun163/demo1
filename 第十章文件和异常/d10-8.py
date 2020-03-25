#练习10-8
fielname=['ds.txt','ds1.txt','re1.txt']
for name in fielname:#遍历列表
    print('文件包含内容：'+name)
    try:#处理异常
        with open(name,'r',encoding='UTF-8')as f:#rb,转为二进制
           con= f.read()#读取列表文件
           # print(con)
    except FileNotFoundError:
        # print(name+"不存在")
        pass#不处理，直接沉默不返回
    else:
        print(con)
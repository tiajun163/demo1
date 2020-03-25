#练习10-10，处理文件内容
finename='re.txt'
with open(finename,encoding='utf-8')as f:
        con=f.read()
        print(con)
        print(con.lower().count('the'))#count()方法查找特定单词出现的次数
        
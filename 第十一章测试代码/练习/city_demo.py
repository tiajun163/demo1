from 第十一章测试代码.练习.ciy_test import ciy_name
print('退出输入q')
while True:
    city=input('输入你城市名退出输入q!\n')
    if city=='q':
        break
    cuntry=input('输入城市大小t退出输入q！\n')
    if cuntry=='q':
        break
    full_name=ciy_name(city,cuntry)
    print('城市详细信息：'+full_name)
    
    
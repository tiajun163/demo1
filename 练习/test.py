sandwich_orders=['nr','bc','ml','pastrami','pastrami','pastrami']#c创建列表包含3个元素
sandich=[]#创建一个空列表

while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')#b
    # print(sandwich_orders)
print(sandwich_orders)
print('没有pastrami三明治')
for sandwich_orders in sandwich_orders:
    print(sandwich_orders.title())
# print("没有pastrami三明治了")
# while sandwich_orders:
#     stset=sandwich_orders.pop()
#     print('三明治1：'+stset.title())
#     sandich.append(stset)
#     print('sandich列表元素：',sandich)
#     for sandich in sandich:
#         print("我要的三明治："+sandich.title())
#     stest=sandwich_orders.pop() #每次删除掉列表最后一个值，赋值给stest
#     print("三明治："+stest.title())
#     sandich.append(stest)#把值添加到列表中
# print(sandich)#打印列表
# for sandich in sandich:#遍历列表输出元素
#     print("我要这个三明治;"+sandich.title())
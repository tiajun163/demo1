def test(name_l):
    print('早上好'+name_l.title())
test('xiaode')
def favorite_book(titles):
    print('你要的书名：'+titles.title())
favorite_book(input("请输入你的书名："))
#传多个参数
def fbook(name,price):
    print(name.title()+'书名')
    print(price+'价格')
fbook('yj','25')
fbook('ss','89')
fbook(input('请输入书名'),input('输入价格'))
#关键字实参
def describe_pet(animal_type,pet_name):
    print("动物类型;"+animal_type)
    print("动物名字"+pet_name.title())
describe_pet(animal_type='猫',pet_name='jik')
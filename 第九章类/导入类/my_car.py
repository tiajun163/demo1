from 第九章类.导入类.Car import Cars
from 第九章类.导入类.Car import ElectricCar
#创建汽车实例
# my_new_car=Cars('宝马','X5',2020)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading=8000
# my_new_car.rad_odometer()
#创建电动车实例
my_tesla=ElectricCar('比亚迪','S5',2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
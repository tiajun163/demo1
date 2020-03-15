class Dog():
        def __init__(self,name,age):
            #'''初始化类的属性''''
            self.name=name
            self.age=age
        def get_set( self ):
            #调用描述狗的方法
            get_sets="小狗叫："+self.name.title()+'今年'+str(self.age)+'岁'
            return  get_sets
godset=Dog('t唐门',25)
print(godset.get_set())

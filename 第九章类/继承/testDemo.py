# ''''重写类方法'''''
#
#
# class test (object):
#     def __init__ ( self ):
#         self.age = 100
#
#     def css ( self ):
#         nameage = self.age
#         print ('你二大爷' + nameage)
#         return nameage
#
#     def si ( self ):
#         print ("qiu")
#
#
# # my=test('100')
# # my.css()
# class demo (test):
#     def __init__ ( self):
#         super ().__init__ (self)
#
#     def si ( self ):
#         print ("土豪")
#
# my = demo ()
# my.si ()
class A (object):
    def __init__ ( self ):
        self.namea = "aaa"
    
    def funca ( self ):
        print ("function a : %s" % self.namea)


class B (A):
    def __init__ ( self ):
        # 这一行解决问题
        super (B, self).__init__ ()
        self.nameb = "bbb"
    
    def funcb ( self ):
        print ("function b : %s" % self.nameb)


b = B ()
# print (b.nameb)
b.funcb ()

b.funca ()
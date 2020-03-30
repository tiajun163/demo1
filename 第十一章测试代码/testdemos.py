import unittest
from 第十一章测试代码.testdemo import get_name

class MyTestCase (unittest.TestCase):
    def test_something ( self ):
        full_naeml=get_name('ss','ewe')
        
        self.assertEqual (full_naeml,'Ssewe')#断言


if __name__ == '__main__':
    unittest.main ()

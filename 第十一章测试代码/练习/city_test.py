import unittest

from  第十一章测试代码.练习 .city_demo import ciy_name
class MyTestCase (unittest.TestCase):
    def test_something ( self ):
        full_names=ciy_name('长沙','5000w')
        self.assertEqual (full_names, '长沙5000w')
    def test_city( self ):
        full_names=ciy_name('nan','ewdr','500w')
        self.assertEqual(full_names,'nanewdr500w')

if __name__ == '__main__':
    unittest.main ()

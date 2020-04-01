import  unittest
# from 第十一章测试代码.testclass import testclassdemo
#创建测试类
from 第十一章测试代码.testclass.testclassdemo import AnonySurvey


class TestAnouysurvey(unittest.TestCase):
    #使用setUp()方法
    def setUp(self):
        #创建一个调查对象和一组答案，供使用的测试方法使用
        question='你学的什么语音'
        self.my_survey=AnonySurvey(question)#创建一个调查对象
        self.responses=['英语','法语','汉语']#创建一组答案
    def test_stors( self ):
        #单个测试答案
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_stores( self ):
        #多个测试答案
        for re in self.responses:#遍历列表
            self.my_survey.store_response(re)
        for re in self.responses:
            self.assertIn(re,self.my_survey.responses)#断言答案是否存在列表中
        
        
    #测试单个答案并存储
    def test_stor( self ):
        question='你学什么语言'
        my_survey=AnonySurvey(question)
        my_survey.store_response('汉语')
        self.assertIn('汉语',my_survey.responses)
    #测试多个
    def test_store( self ):
        question="你学什么语言"
        my_survey=AnonySurvey(question)
        resp=['英语','法语','汉语']
        for re in resp:
                my_survey.store_response(re)
        for re in resp:
            self.assertIn(re,my_survey.responses)
# unittest.main()
if __name__=='main()':
    unittest.main()
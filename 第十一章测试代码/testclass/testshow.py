import  unittest
# from 第十一章测试代码.testclass import testclassdemo
#创建测试类
from 第十一章测试代码.testclass.testclassdemo import AnonySurvey


class TestAnouysurvey(unittest.TestCase):
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
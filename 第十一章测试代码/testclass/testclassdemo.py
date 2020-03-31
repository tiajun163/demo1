#创建测试类
class AnonySurvey():
    
    def __init__(self,question):
        #初始化类属性 存储一个问题，并为存储答案做准备
        self.question=question
        self.responses=[]
    def show_question( self ):
        #显示调查问卷
        print(self.question)
    def store_response( self ,now_response):
        #存储单份调查答案
        self.responses.append(now_response)
    def show_results( self ):
        #显示手机到的所有答案
        print('收集的答案！')
        for response in self.responses:
            print('_'+response)
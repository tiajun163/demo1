from  第十一章测试代码.testclass import  testclassdemo
#定义一个问题，并创建一个调查AnonySurvey对象
question=('你学什么语言！：')
my_survey=testclassdemo.AnonySurvey(question)
#显示问题并存储答案
my_survey.show_question()
print("退出输入q:\n")
while True:
    response = input("输入语言：\n")
    
    if response=='q':
        break
    my_survey.store_response(response)
#打印调查结果
print('调查结果：\n')
my_survey.show_results()
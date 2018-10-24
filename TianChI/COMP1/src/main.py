import TrainDataReadAnn
import Classifier
import dataFormter
import dividedWord
import jieba
import os

# # ?Step1: Get the ann for all traindata
# traindatapath = "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/ruijin_round1_train2_20181022"
# massage = TrainDataReadAnn.readAnn(traindatapath, "TrainDataAnn.db")
# print(massage)

# # ?Step2: Divided the word
# testpath = "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/ruijin_round1_test_a_20181022"
# trananndabase = "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/TrainDataAnn.db"
# massage = dividedWord.divided(testpath)
# print(massage)

# # ?Step3:Classifier
# massage = Classifier.judgement()
# print(massage)

# ? Step3:Give ans
massage = dataFormter.dataopener(
    "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/ans.db", "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/ruijin_round1_submit_20181022", "ANS")
print(massage)

#s5111611
"""
IMPORTANT: unfortunetly during the implementation of the for row in k: loop to run the
machine learning algorythm more then once to collect more data, a problem has oocured where somtimes on chance the program will
crash with an error ValueError: max() arg is an empty sequence which i didnt have enought
time to fix or find the issue, if you run into this error please just run the code again and it should work
thank you :)

"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.impute import KNNImputer
import CART as CR
from sklearn import datasets
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
names=["Age","Gender","Chest Pain Type","Resting blood pressure","Serum cholesterol","Fasting blood sugar","Resting electrocardiographic","Maximum heart rate achieved","Exercise induced angina","ST depression","exercise ST segment","The number of major vessels" ,"Thalassemia","Target"]
dataset1 = pd.read_csv ('heart-disease.data',header=None, names=names)

dataset_nan=dataset1.replace('?', np.NaN)


int_f=["Age","Gender","Chest Pain Type","Resting blood pressure","Serum cholesterol","Fasting blood sugar","Resting electrocardiographic","Maximum heart rate achieved","Exercise induced angina","exercise ST segment","The number of major vessels" ,"Thalassemia","Target"]
float_f=["ST depression"]

dataset_nan[float_f+int_f]=dataset_nan[float_f+int_f].apply(pd.to_numeric, downcast="float")

for names in int_f :
    dataset_nan[names]= pd.array(dataset_nan[names].values,dtype=pd.Int64Dtype())
dataset_nan=dataset_nan.drop(["exercise ST segment", "The number of major vessels","Thalassemia"], axis=1)

st_depression_mode = depression_mode = dataset_nan['ST depression'].value_counts().index[0]
dataset_nan.fillna({'ST depression' : st_depression_mode}, inplace=True)

dataset_nan.interpolate(method='pad', inplace=True)


k=[0,1,2,3,4]
acc=list()
con=list()
f1=list()

for row in k:
    
    train,test = train_test_split(dataset_nan, test_size=0.3)
    train=train.values.tolist()
    test=test.values.tolist()

    max_depth = 6
    min_size = 8

    predicted = CR.init(train,test, max_depth, min_size)


    def actual_y():
        actual= list()
        x=0
        while x != len(test):
            actual.append(test[x][10])
            x=x+1   
        return actual

    actual=actual_y()

    accuracy = metrics.accuracy_score(actual, predicted)
    confu=metrics.confusion_matrix(actual, predicted)
    f_score = metrics.f1_score(actual,predicted, average='weighted', labels=np.unique(predicted))
    acc.append(accuracy)
    con.append(confu)
    f1.append(f_score)
print('acc:',acc)
k=sum(con)
print(k)
print('f1:',f1)



   
    


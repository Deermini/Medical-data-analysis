# !usr/bin/env python
# -*- coding:utf-8 -*-

import sklearn.decomposition
from GCForest import *
from skmultilearn.adapt import MLkNN
from skmultilearn.neurofuzzy import MLARAM
from skmultilearn.problem_transform import BinaryRelevance
from skmultilearn.problem_transform import LabelPowerset,ClassifierChain
from skmultilearn.ensemble.rakeld import RakelD
from skmultilearn.ensemble.rakelo import RakelO
import sklearn.metrics
from skmultilearn.dataset import Dataset
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.svm import SVC,LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import BernoulliRBM,MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression,SGDClassifier
from numpy import *
import csv
from sklearn.externals import joblib
from scipy.sparse import csc_matrix

"""用于区分计算（A,B,C,D,E）各项检查，label.txt是用于建立索引的"""
f=open("F:/test/medical/prescribe_record.csv","r")
content=csv.reader(f)
TAG_label=[]
index_label=[]
for i,row in enumerate(content):
    if i==0:
        continue
    else:
        if row[5]=="A":
            TAG_label.append(row[8])
        # if row[5]=="C02":
        #     TAG_label.append(row[8])

"""把不同种类的检查写入文件"""
# #print(TAG_label)
# TAG_label2=sorted(set(TAG_label))
# f_label=open("F:/medical_result/label_C.txt","w")
# for li in TAG_label2:
#     f_label.write(li+"\n")

f1=open("label.txt","r")
content1=f1.readlines()
label=[]
for row in content1:
    row=row.split()[1]
    label.append(row)
#print(label)

for i in sorted(set(TAG_label)):
    i="TAG_"+i
    index_label.append(label.index(i))

# print(index_label)
print(len(index_label),len(set(TAG_label)))

"""用多标记学习进行预测"""
k =[];k1=[]
k2=[];k3=[]
labelcount =1853
endianness = 'little'
feature_type = 'float'
encode_nominal = True
load_sparse = True
X, y1 = Dataset.load_arff_to_numpy("medical_data2.arff",
                                  labelcount=labelcount,
                                  endian="little",
                                  input_feature_type=feature_type,
                                  encode_nominal=encode_nominal,
                                  load_sparse=load_sparse)


y1=y1.toarray()
#index_label=[0,1,2,3,4,5,6,7,8,9,10]
y=y1[:,index_label]
y=csc_matrix(y)
# classifier= LabelPowerset(MultinomialNB(), require_dense=[True, True])
# clf=RakelD(classifier,labelset_size=11)
# clf.fit(X, y)
# joblib.dump(clf, 'F:/medical_result/cure_after/filename2.pkl')
clf = joblib.load('F:/medical_result/medical_A/filename.pkl')
#print "X[0]:",X[0]
for i in range(90):
    predictions = clf.predict(X[i])
    #将预测值和真实值作对比观察
    pre=predictions.tocsr()
    print "--------------------------"
    print i
    print pre
    print
    print y[i]
    print "--------------------------"

predictions = clf.predict(X[:90])
f1score= sklearn.metrics.f1_score(y[:90].toarray(), predictions.toarray(),average='micro')
print "f1score:",f1score



"""
#注意一下feature0.txt里面只有1960个特征，这个地方有个问题要解决掉，把feature0.txt里面弄成1977个特征

feature_dict={}
id=0
f=open("F:/medical_result/feature0.txt","r")
for li in f.readlines():
    li=li.split()[0]
    feature_dict[li]=id
    id+=1
f.close()
joblib.dump(feature_dict,"F:/medical_result/feature0_dict.pkl")
feature_dict=joblib.load("F:/medical_result/feature0_dict.pkl")

f2=open("F:/medical_result/label_y.txt")
label=[]
for li in f2.readlines():
    li=li.split()[0]
    label.append(li)
joblib.dump(label,"F:/medical_result/label_y.pkl")
label=joblib.load("F:/medical_result/label_y.pkl")


f0=open('F:/medical_result/label_A.txt','r')
label_A=[]
for li in f0.readlines():
    label_A.append(li.strip())
joblib.dump(label_A,"F:/medical_result/label_A.pkl")
label_A=joblib.load("F:/medical_result/label_A.pkl")


"""
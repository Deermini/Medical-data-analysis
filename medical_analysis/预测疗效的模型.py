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
f=open("F:/test/prescribe_record.csv","r")
content=csv.reader(f)
TAG_label=[]
index_label=[]
for i,row in enumerate(content):
    if i==0:
        continue
    else:
        if row[5]=="C01":
            TAG_label.append(row[8])
        if row[5]=="C02":
            TAG_label.append(row[8])
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

#对数据进行降维
# X = X.toarray()
# pca = sklearn.decomposition.PCA(n_components=8)
# newX = pca.fit_transform(X)
# #简单可视化分析
# import pylab as pl
# px=newX[:,0]
# py=newX[:,1]
# pl.plot(px,py,".r")
# pl.show()
index=[0,1,2,3,4,5,6,7,8,9,10]
classifier= LabelPowerset(MultinomialNB(), require_dense=[True, True])
clf=RakelO(classifier,labelset_size=8,model_count=1600)
clf.fit(X, y1)
joblib.dump(clf, 'F:/medical_result/cure_after/filename.pkl')
clf = joblib.load('F:/medical_result/cure_after/filename.pkl')
#print "X[0]:",X[0]
for i in range(90):
    predictions = clf.predict(X[i])
    #将预测值和真实值作对比观察
    #pre=predictions.tocsr()
    print "--------------------------"
    print list(predictions.toarray()[i,index]).index(1)
    print
    print list(y1.toarray()[i,index]).index(1)
    print "--------------------------"









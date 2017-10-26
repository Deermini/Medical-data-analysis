# !usr/bin/env python
# -*- coding:utf-8 -*-

from skmultilearn.adapt import MLkNN
from skmultilearn.neurofuzzy import MLARAM
from skmultilearn.problem_transform import BinaryRelevance
from skmultilearn.problem_transform import LabelPowerset,ClassifierChain
from skmultilearn.ensemble.rakeld import RakelD
from skmultilearn.ensemble.rakelo import RakelO
import sklearn.metrics
from skmultilearn.dataset import Dataset
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import BernoulliRBM,MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression,SGDClassifier
from numpy import *
import csv

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
#print(TAG_label)

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
# print(len(index_label),len(set(TAG_label)))

"""用多标记学习进行预测"""
k = [];k1=[]
k2=[];k3=[]
labelcount =1853
endianness = 'little'
feature_type = 'float'
encode_nominal = True
load_sparse = True
X, y = Dataset.load_arff_to_numpy("medical_data2.arff",
                                  labelcount=labelcount,
                                  endian="little",
                                  input_feature_type=feature_type,
                                  encode_nominal=encode_nominal,
                                  load_sparse=load_sparse)
X=X.toarray()
sum=0
for li in X:
    print list(li).count(1)
    sum+=list(li).count(1)
print 1.0*sum/len(X)

y=y.toarray()
sum=0
for li in y:
    print list(li).count(1)
    sum+=list(li).count(1)
print 1.0*sum/len(y)
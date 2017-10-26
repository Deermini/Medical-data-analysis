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
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression,SGDClassifier
from numpy import *
import csv

"""用于区分计算（A,B,C,D,E）各项检查，label.txt是用于建立索引的"""
f=open("F:/test/prescribe_record.csv","r")
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
k =[];k1=[]
k2=[];k3=[]
labelcount =1842
endianness = 'little'
feature_type = 'float'
encode_nominal = True
load_sparse = True
X, y = Dataset.load_arff_to_numpy("medical_data.arff",
                                  labelcount=labelcount,
                                  endian="little",
                                  input_feature_type=feature_type,
                                  encode_nominal=encode_nominal,
                                  load_sparse=load_sparse)

#利用关联分析，对疾病进行挖掘
print "X[0]:",X[0].toarray()[0]
X1=X[0].toarray()[0]
index=[]
for i,li in enumerate(X1):
    if li==1:
        index.append(str(i))
print "index:",index

#获取index所有可能的组合,因为考虑到最多只有频繁5项集，所以用了range(1,6).
prob_result=[]
list2 = []
for i in range(1,6):
    iter = itertools.combinations(index,i)
    list2.extend(list(iter))
for li in list2:
    li=",".join(li)
    prob_result.append(str(li))
print "prob_result:",prob_result

#找出概率最大的几个事件
f2=open("result_sorted.txt","r")
index_dict={}
for li in f2.readlines():
    li=li.split("--->")
    index_dict[li[0]]={}
    index_dict[li[0]]["X"]=li[1]
    index_dict[li[0]]["y"]=li[2].strip()
print "index_dict:",index_dict

refer_to={}
for li in prob_result:
    if li not in index_dict.keys():
        continue
    else:
        value=index_dict[li]
        refer_to[value["X"]]=value["y"]

refer_to_sorted = sorted(refer_to.items(), key=lambda x: x[1], reverse=True)
#print "refer_to_sorted:",refer_to_sorted
k=3
if len(refer_to_sorted)==0:
    pass
elif len(refer_to_sorted)>0 and len(refer_to_sorted)<k:
    for i in range(len(refer_to_sorted)):
        print "refer_to_sorted:",refer_to_sorted[i]
else:
    for i in range(k):
        print "refer_to_sorted:",refer_to_sorted[i]







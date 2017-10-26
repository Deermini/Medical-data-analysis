# !usr/bin/env python
# -*- coding:utf-8 -*-

import sklearn.decomposition
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
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression,SGDClassifier
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
        if row[5]=="E":
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

# #对数据进行降维
# from sklearn.decomposition import TruncatedSVD
# #print X
# X = X.toarray()
# svd = TruncatedSVD(n_components=10, n_iter=7, random_state=42)
# newX = svd.fit_transform(X)
#
# X = X.toarray()
# pca = sklearn.decomposition.PCA(n_components=8)
# newX = pca.fit_transform(X)
#
# # #简单可视化分析
# # import pylab as pl
# # px=newX[:,0]
# # py=newX[:,1]
# # pl.plot(px,py,".r")
# # pl.show()

#y=y1[:,index_label]
n_splits=10
labelcount1=5
#进行10次10折交叉
for j in range(1):
    #对数据进行10折交叉验证
    kf = KFold(n_splits=n_splits, random_state=33, shuffle=True)
    for train_index, test_index in kf.split(X, y1):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y1[train_index], y1[test_index]

        classifier= LabelPowerset(MultinomialNB(), require_dense=[True, True])
        clf=RakelD(classifier,labelset_size=labelcount1)
        #clf=RakelO(classifier,labelset_size=labelcount1,model_count=1000)
        #clf=MLkNN()

        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)

        #将预测值和真实值作对比观察
        pre=predictions.tocsr()
        for li in range(0,10,1):
            print pre[li,:]
            print
            print y_test[li,:]
            print "--------------------------"

        hammingloss= sklearn.metrics.hamming_loss(y_test, predictions)
        jaccard= sklearn.metrics.jaccard_similarity_score(y_test, predictions)
        f1score= sklearn.metrics.f1_score(y_test, predictions,average='micro')
        zerooneloss= sklearn.metrics.zero_one_loss(y_test, predictions)
        print "hammingloss,jaccard,f1score,zerooneloss:", hammingloss, jaccard, f1score, zerooneloss
        k.append(hammingloss)
        k1.append(jaccard)
        k2.append(zerooneloss)
        k3.append(f1score)

from numpy import *
print("hamming_loss mean:", array(k).mean())
print("hamming_loss var:", array(k).var())

print("jaccard mean:",array(k1).mean())
print("jaccard var:", array(k1).var())

print("f1_score mean:", array(k3).mean())
print("f1_score var:", array(k3).var())

print("zero_one_loss mean:", array(k2).mean())
print("zero_one_loss var:", array(k2).var())

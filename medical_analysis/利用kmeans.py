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
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
import scipy.cluster.hierarchy as hcluster


"""用于区分计算（A,B,C,D,E）各项检查，label.txt是用于建立索引的"""
f=open("F:/test/prescribe_record.csv","r")
content=csv.reader(f)
TAG_label=[]
index_label=[]
for i,row in enumerate(content):
    if i==0:
        continue
    else:
        if row[5]=="D":
            TAG_label.append(row[8])
        # if row[5]=="A":
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

X=X.toarray()
#kmeans=KMeans(n_clusters=13,random_state=0).fit(X)
kmeans2=hcluster.fclusterdata(X, criterion='maxclust', t=12)
#kmeans = SpectralClustering(n_clusters=8).fit(X)
#print kmeans.labels_
index_0=[];index_1=[];index_2=[];index_3=[];index_4=[];index_5=[]
for i,li in enumerate(kmeans2):
    if li==0:
        index_0.append(i)
    elif li==1:
        index_1.append(i)
    elif li==2:
        index_2.append(i)
    elif li==3:
        index_3.append(i)
    elif li==4:
        index_4.append(i)
    elif li==5:
        index_5.append(i)
print len(index_0)
print len(index_1)
print len(index_2)
print len(index_3)
print len(index_4)
print len(index_5)
index=index_5

y1=y1.toarray()
y=y1[:,index_label]
y=csc_matrix(y)
classifier= LabelPowerset(MultinomialNB(), require_dense=[True, True])
clf=RakelO(classifier,labelset_size=6,model_count=800)
clf.fit(X[index[100:]], y[index[100:]])
# joblib.dump(clf, 'F:/medical_result/cure_after/filename.pkl')
# clf = joblib.load('F:/medical_result/cure_after/filename.pkl')
#print "X[0]:",X[0]
predictions = clf.predict(X[index[:100]])
#将预测值和真实值作对比观察
pre=predictions.tocsr()
for i in range(100):
    print "--------------------------"
    print pre[i]
    print
    print y[index_0[i]]
    print "--------------------------"


f1score= sklearn.metrics.f1_score(y[index[:100]].toarray(), predictions.toarray(),average='micro')
print "f1score:",f1score



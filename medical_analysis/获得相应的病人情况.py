# !usr/bin/env python
# -*- coding:utf-8 -*-
#
# import sklearn.decomposition
# from GCForest import *
# from skmultilearn.adapt import MLkNN
# from skmultilearn.neurofuzzy import MLARAM
# from skmultilearn.problem_transform import BinaryRelevance
# from skmultilearn.problem_transform import LabelPowerset,ClassifierChain
# from skmultilearn.ensemble.rakeld import RakelD
# from skmultilearn.ensemble.rakelo import RakelO
# import sklearn.metrics
# from skmultilearn.dataset import Dataset
# from sklearn.naive_bayes import GaussianNB,MultinomialNB
# from sklearn.svm import SVC,LinearSVC
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.neural_network import BernoulliRBM,MLPClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
# from sklearn.model_selection import KFold
# from sklearn.linear_model import LogisticRegression,SGDClassifier
# from numpy import *
# import csv
# from sklearn.externals import joblib
# from scipy.sparse import csc_matrix
#
# """用于区分计算（A,B,C,D,E）各项检查，label.txt是用于建立索引的"""
# f=open("F:/test/prescribe_record.csv","r")
# content=csv.reader(f)
# TAG_label=[]
# index_label=[]
# for i,row in enumerate(content):
#     if i==0:
#         continue
#     else:
#         if row[5]=="A":
#             TAG_label.append(row[8])
#         # if row[5]=="C02":
#         #     TAG_label.append(row[8])
# """把不同种类的检查写入文件"""
# # #print(TAG_label)
# # TAG_label2=sorted(set(TAG_label))
# # f_label=open("F:/medical_result/label_C.txt","w")
# # for li in TAG_label2:
# #     f_label.write(li+"\n")
#
# f1=open("label.txt","r")
# content1=f1.readlines()
# label=[]
# for row in content1:
#     row=row.split()[1]
#     label.append(row)
# #print(label)
#
# for i in sorted(set(TAG_label)):
#     i="TAG_"+i
#     index_label.append(label.index(i))
#
# # print(index_label)
# print(len(index_label),len(set(TAG_label)))
#
# """用多标记学习进行预测"""
# k =[];k1=[]
# k2=[];k3=[]
# labelcount =1853
# endianness = 'little'
# feature_type = 'float'
# encode_nominal = True
# load_sparse = True
# X, y1 = Dataset.load_arff_to_numpy("medical_data2.arff",
#                                   labelcount=labelcount,
#                                   endian="little",
#                                   input_feature_type=feature_type,
#                                   encode_nominal=encode_nominal,
#                                   load_sparse=load_sparse)
#
#
# new_x=X.toarray()[75]
# f=open("F:/medical_result/feature0.txt")
# feature=[]
# for li in f.readlines():
#     li=li.split()[0]
#     feature.append(li)
# for i,li in enumerate(new_x):
#     if li ==1:
#         print feature[i],


f1=open("F:/test/diag1.txt")
f2=open("F:/test/diag2.txt")
#f3=open("F:/test/diag3.txt","w")
dict={}
diag1=[];diag2=[]
for li in f1.readlines():
    if li=="\n":
        li="1234566789909"
        diag1.append(li)
    else:
        li=li.split()[0]
        diag1.append(li)
for li in f2.readlines():
    if li=="\n":
        li="1234566789909"
        diag2.append(li)
    else:
        li=li.split()[0]
        diag2.append(li)
print len(diag1),len(diag2)
for i,li in enumerate(diag1):
    if li not in dict.keys():
        dict[li]=diag2[i]

print dict['P59.901']

# f=open("F:/medical_result/label_D.txt")
# label_A=[]
# for li in f.readlines():
#     li=li.split()[0]
#     label_A.append(li)
#
# index=[149,150,175,189,340,381,389,390,392,469,514]
# index2=[13,69,149,150,175,176,189,340,381,389,390,392,469,514,515]
# print "预测：",
# for i in index:
#     print label_A[i],
# print
#
# print "真实值：",
# for i in index2:
#     print label_A[i],
# print
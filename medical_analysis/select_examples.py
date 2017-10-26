# !usr/bin/env python
# -*- coding:utf-8 -*-

from skmultilearn.dataset import Dataset
from sklearn.externals import joblib

"""筛选出一些较好的样例进行预测，主要是把每个样例的病情弄清楚"""
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

"""存储相应的特征"""
feature=[]
f=open("feature0.txt","r")
for li in f.readlines():
    li=li.split()[0]
    feature.append(li)

"""这个索引是在存模型的时候挑选出来"""
index=[5,15,18,19,20,25,31,35,38,48,54,59,60,67,73,75,85,87,89]
diag_to_chinese_dict = joblib.load('F:/medical_result/diag_to_chinese_dict.pkl')

X=X.toarray()
new_X=X[index,:]
for li in new_X:
    feature_X = []
    for i,lj in enumerate(li):
        if lj==1:
            feature_X.append(feature[i])
    #print(feature_X)
    for j in feature_X:
        if j in diag_to_chinese_dict.keys():
            print diag_to_chinese_dict[j],

    print


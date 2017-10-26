# !usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import numpy as np
from sklearn.externals import joblib
from scipy.sparse import csc_matrix
from sklearn.neighbors import NearestNeighbors

"""生成数据,生成数据后可跳过此步骤"""
"""
f=open("F:/test/medical/case_diag.csv",'r')
content=csv.reader(f)
data={}
for i,li in enumerate(content):
    if i ==0:
        pass
    elif li[1] not in data.keys():
        data[li[1]]={}
        data[li[1]]["X"]={}
        data[li[1]]["X"]["age"] ="age.6_10"
        data[li[1]]["X"]["diag"] = []
        data[li[1]]["X"]["diag"].append(li[3])
        data[li[1]]["X"]["cure_before"]="cure_before.%s"%(li[4])
    else:
        data[li[1]]["X"]["diag"].append(li[3])
f.close()
print(data["277775008"])

f2=open("F:/test/medical/case_residence.csv","r")
content2=csv.reader(f2)
for i,li in enumerate(content2):
    if i==0:
        pass
    if li[1] in data.keys():
        if "岁" in li[3]:
            age=int(li[3].split("岁")[0])
            if age>15:
                data[li[1]]["X"]["age"]="age.15_"
            elif age>10:
                data[li[1]]["X"]["age"] = "age.10_15"
            elif age>6:
                data[li[1]]["X"]["age"] = "age.6_10"
            elif age>3:
                data[li[1]]["X"]["age"] = "age.3_6"
            elif age>1:
                data[li[1]]["X"]["age"]="age.1_3"
            else:
                data[li[1]]["X"]["age"] = "age.0_1"
        else:
            print i, li[3]
            data[li[1]]["X"]["age"] ="age.0_1"

f2.close()
print(len(data.keys()))

#建立特征的索引
f3=open('feature0.txt','r')
feature={};id=0
for li in f3.readlines():
    li=li.split()[0]
    feature[li]=id
    id+=1
f3.close()
print(feature)

dataset_X=[]
examples_index=[]
for li in data.keys():
    X = np.zeros(1977)
    examples_index.append(int(li))
    X[feature[data[li]["X"]["cure_before"]]]=1
    X[feature[data[li]["X"]["age"]]] = 1
    for lj in data[li]["X"]["diag"]:
        if lj in feature.keys():
            X[feature[lj]]= 1
    dataset_X.append(X)

input_X=np.array(dataset_X)

#存储数据
joblib.dump(examples_index,"F:/medical_result/examples_index.pkl")
joblib.dump(input_X,"F:/medical_result/input_X.pkl")

print(input_X.shape)
print(examples_index[:10])
"""
input_X=joblib.load("F:/medical_result/input_X.pkl")
example_index=joblib.load("F:/medical_result/examples_index.pkl")

d=[]
for i in range(1977):
    if i <17:
        d.append(5.0)
    else:
        d.append(1.0)

X=csc_matrix(input_X/d)
knn = NearestNeighbors().fit(X)
joblib.dump(knn, 'F:/medical_result/distance_index/filename2.pkl')
knn = joblib.load('F:/medical_result/distance_index/filename2.pkl')
result=knn.kneighbors(X[89], 8, return_distance=True)
distance=result[0][0]
kneighbors_index=[]
for li in result[1][0]:
    kneighbors_index.append(example_index[li])
print kneighbors_index
# !usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import numpy as np
from sklearn.externals import joblib


"""生成数据"""
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
        if li[4]=='':
            li[4]=2
        data[li[1]]["X"]["cure_before"]="cure_before.%s"%(abs(int(li[4])))
        data[li[1]]["Y"]={}
        data[li[1]]["Y"]["drug"] = []
        if li[6]=='':
            li[6]=3
        data[li[1]]["Y"]['cure_after'] ="TAG_cure_after.%s"%(abs(int(li[6])))
    else:
        data[li[1]]["X"]["diag"].append(li[3])
        if li[6]=='' or not li[6].isdigit():
            li[6]=3
        data[li[1]]["Y"]["cure_after"]="TAG_cure_after.%s"%(abs(int(li[6])))
f.close()
print(len(data.keys()))

f1=open("F:/test/medical/prescribe_record.csv","r")
content1=csv.reader(f1)
for i,li in enumerate(content1):
    if i==0:
        pass
    elif li[4] not in data.keys():
        pass
    else:
        data[li[4]]["Y"]["drug"].append(li[8])
f1.close()
print(len(data.keys()))

f2=open("F:/test/medical/case_residence.csv","r")
content2=csv.reader(f2)
for i,li in enumerate(content2):
    if i==0:
        pass
    if li[1] not in data.keys():
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
            data[li[1]]["X"]["age"] ="age.0_1"

f2.close()
print(len(data.keys()))

"""建立特征的索引"""
f3=open('feature0.txt','r')
feature={};id=0
for li in f3.readlines():
    li=li.split()[0]
    feature[li]=id
    id+=1
f3.close()

"""建立标签的索引"""
f4=open("label.txt","r")
label={};id=0
for li in f4.readlines():
    li=li.split()[1]
    label[li]=id
    id+=1
f4.close()


dataset_X=[]
dataset_y=[]
examples_index=[]
for li in data.keys():
    X = np.zeros(1977)
    y = np.zeros(1853)
    examples_index.append(int(li))
    X[feature[data[li]["X"]["cure_before"]]]=1
    #X[feature[data[li]["X"]["age"]]] = 1
    for lj in data[li]["X"]["diag"]:
        if lj in feature.keys():
            X[feature[lj]]= 1

    y[label[data[li]["Y"]["cure_after"]]]=1
    for lj in data[li]["Y"]["drug"]:
        lj="TAG_"+lj
        y[label[lj]]=1
    dataset_X.append(X)
    dataset_y.append(y)

input_X=np.array(dataset_X)
input_y=np.array(dataset_y)

"""存储数据"""
#joblib.dump(examples_index,"F:/medical_result/examples_index.pkl")
joblib.dump(input_X,"F:\project_files\medical_analysis\input_X.pkl")
joblib.dump(input_y,"F:\project_files\medical_analysis\input_y.pkl")

input_data=np.hstack((input_X,input_y))
np.save("F:\project_files\medical_analysis\input_data",input_data)

print(input_X.shape)
print(input_y.shape)
print(examples_index[:10])






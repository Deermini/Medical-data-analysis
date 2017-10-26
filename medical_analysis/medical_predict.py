# !usr/bin/env python
# -*- coding:utf-8 -*-
import itertools
from numpy import *
from sklearn.externals import joblib
from scipy.sparse import csc_matrix

def selection(content):
    for li in content:
        if "葡萄糖" in li:
            pass
        elif "氯化钠" in li:
            pass
        elif "氯化钾" in li:
            pass
        elif "灭菌注射用水" in li:
            pass
        else:
            print li.decode('utf-8'),
    print

def selection2(content):
    for li in content:
        print li.decode('utf-8'),
    print

diag_to_chinese_dict = joblib.load('F:/medical_result/diag_to_chinese_dict.pkl')

"三个输入参数"
age=int(input("age:"))
cure_before=int(input("cure_before:"))
diag=raw_input("diag:")
print

feature=[]
"""转换年龄数据"""
if age<=1:
    age="age"+".0_1"
elif age<=3:
    age = "age" + ".1_3"
elif age <= 6:
    age = "age" + ".3_6"
elif age <= 10:
    age = "age" + ".6_10"
elif age <= 15:
    age = "age" + ".10_15"
else:
    age = "age" + ".15_"
feature.append(age)
print "feature:",age,

"""转换cure_before数据"""
cure_before="cure_before."+str(cure_before)
feature.append(cure_before)
print cure_before,
"""转换diag数据"""
diag=diag.strip().split(",")
feature.extend(set(diag))
for li in set(diag):
    print diag_to_chinese_dict[li],
print

"""注意一下feature0.txt里面只有1960个特征，这个地方有个问题要解决掉，把feature0.txt里面弄成1977个特征"""
feature_dict=joblib.load("F:/medical_result/feature0_dict.pkl")

X=zeros(1977)
#print "X",X
for li in feature:
    if li in feature_dict.keys():
        X[feature_dict[li]]=1

d=[]
for i in range(1977):
    if i <17:
        d.append(5.0)
    else:
        d.append(1.0)
X1=csc_matrix(X/d)
X=csc_matrix(X)

"找到最相近的几个处方"
input_X=joblib.load("F:/medical_result/input_X.pkl")
example_index=joblib.load("F:/medical_result/examples_index.pkl")

d=[]
for i in range(1977):
    if i <17:
        d.append(5.0)
    else:
        d.append(1.0)
knn = joblib.load('F:/medical_result/distance_index/filename2.pkl')
result=knn.kneighbors(X1, 6, return_distance=True)
kneighbors_distance=result[0][0]
kneighbors_index=[]
for li in result[1][0]:
    kneighbors_index.append(example_index[li])
print "最近几个样例的距离：",kneighbors_distance
print "最近的几个病历号：",kneighbors_index

"""
knn = joblib.load('F:/medical_result/distance_index/filename2.pkl')
y1 = joblib.load('F:/medical_result/y1/filename.pkl')
distance_index=knn.kneighbors(X1, 5, return_distance=True)

label=joblib.load("F:/medical_result/label_y.pkl")
result_1=[];result_2=[];result_3=[];result_4=[];result_5=[]

for j,li in enumerate(list(distance_index[1][0])):
    for i,li2 in enumerate(y1[li]):
        if li2==1:
            if j==1:
                result_1.append(label[i])
            elif j==2:
                result_2.append(label[i])
            elif j==3:
                result_3.append(label[i])
            elif j==4:
                result_4.append(label[i])
            else:
                result_5.append(label[i])

print "result_1:",result_1[0],
selection(set(result_1[1:]))

print "result_2:",result_2[0],
selection(set(result_2[1:]))

print "result_3:",result_3[0],
selection(set(result_3[1:]))

print "result_4:",result_4[0],
selection(set(result_4[1:]))

print "result_5:",result_5[0],
selection(set(result_5[1:]))
"""

"西药（A）:"
medical0=[]
clf0 = joblib.load('F:/medical_result/medical_A/filename.pkl')
prediction0 = clf0.predict(X)
prediction0=prediction0.toarray()[0]
label_A=joblib.load("F:/medical_result/label_A.pkl")
for i,li in enumerate(prediction0):
    if li!=0:
        medical0.append(label_A[i])

"中成药（B）:"
medical1=[]
clf1 = joblib.load('F:/medical_result/medical_B/filename.pkl')
prediction1 = clf1.predict(X)
prediction1=prediction1.toarray()[0]
label_B=joblib.load("F:/medical_result/label_B.pkl")
for i,li in enumerate(prediction1):
    if li!=0:
        medical1.append(label_B[i])


"中草药（C）:"
medical2=[]
clf2 = joblib.load('F:/medical_result/medical_C/filename.pkl')
prediction2 = clf2.predict(X)
prediction2=prediction2.toarray()[0]
label_C=joblib.load("F:/medical_result/label_C.pkl")
for i,li in enumerate(prediction2):
    if li!=0:
        medical2.append(label_C[i])

"检验（D）:"
medical3=[]
clf3 = joblib.load('F:/medical_result/medical_D/filename.pkl')
prediction3 = clf3.predict(X)
prediction3=prediction3.toarray()[0]
label_D=joblib.load("F:/medical_result/label_D.pkl")
for i,li in enumerate(prediction3):
    if li!=0:
        medical3.append(label_D[i])

"检查（E）:"
medical4=[]
clf4 = joblib.load('F:/medical_result/medical_E/filename.pkl')
prediction4 = clf4.predict(X)
prediction4=prediction4.toarray()[0]
label_E=joblib.load("F:/medical_result/label_E.pkl")
for i,li in enumerate(prediction4):
    if li!=0:
        medical4.append(label_E[i])

"疗效:"
clf8 = joblib.load('F:/medical_result/cure_after/filename.pkl')
predictions = list(clf8.predict(X).toarray()[0])
if 1 in predictions:
    cure_after=predictions.index(1)
else:
    cure_after=3

"""使用关联技术对疾病进行分析"""
X_index=[]
for li in sorted(diag):
    X_index.append(str(li))

#获取index所有可能的组合,因为考虑到最多只有频繁5项集，所以用了range(1,6).
prob_result=[]
list2 = []
for i in range(1,6):
    iter =itertools.combinations(X_index,i)
    list2.extend(list(iter))
for li in list2:
    li=",".join(li)
    prob_result.append(str(li))
#print "prob_result:",prob_result

#找出概率最大的几个事件
index_dict=joblib.load("F:/medical_result/apriori_analysis_dict.pkl")

refer_to=[]
for li in prob_result:
    if li not in index_dict.keys():
        continue
    else:
        value=index_dict[li]
        if len(value)>=5:
            refer_to.extend(value[:5])
        else:
            refer_to.extend(value)

refer_to_sorted = sorted(refer_to, key=lambda x: x[1], reverse=True)
#print(refer_to_sorted)

"""获取几个最有可能潜在的疾病"""
def get_examples(K=None,content=None,refer_to_sorted=None):
    result=[]
    for li in refer_to_sorted:
        content1=li[0].strip().split(",")
        content2 = []
        for lj in content1:
            if lj not in content:
                content.append(lj)
                content2.append(lj)
        if len(content2)!=0:
            result.append((content2,li[1]))
    if len(result)<=K:
        return result
    else:
        return result[:K]

k=6;content=[]
content.extend(diag)
medical5=get_examples(K=k,content=content,refer_to_sorted=refer_to_sorted)

print "西药（A）:",
selection(list(set(medical0)))

print "中成药（B）:",
selection2(list(set(medical1)))

print "中草药（C）:",
selection2(list(set(medical2)))

print "检验（D）:",
selection2(list(set(medical3)))

print "检查（E）:",
selection2(list(set(medical4)))

print "疗效：",cure_after

print "与之相关的疾病有:",medical5
for li in medical5:
    for lj in li[0]:
        print diag_to_chinese_dict[lj],
    print li[1]



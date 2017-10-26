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

"三个输入参数"
age=int(input("age:"))
cure_before=int(input("cure_before:"))
diag=raw_input("diag:")
print

feature=[]
"""转换年龄数据"""
if age<=1:
    age="age"+".0_1"

    feature.append(age)
elif age<=3:
    age = "age" + ".1_3"
    feature.append(age)
elif age <= 6:
    age = "age" + ".3_6"
    feature.append(age)
elif age <= 10:
    age = "age" + ".6_10"
    feature.append(age)
elif age <= 15:
    age = "age" + ".10_15"
    feature.append(age)
else:
    age = "age" + ".15_"
    feature.append(age)
"""转换cure_before数据"""
cure_before="cure_before."+str(cure_before)
feature.append(cure_before)
"""转换diag数据"""
diag=diag.strip().split(",")
#print "diag:",diag
feature.extend(set(diag))
print "feature:",feature

feature_dict={}
id=0
f=open("feature0.txt","r")
for li in f.readlines():
    li=li.split()[0]
    feature_dict[li]=id
    id+=1
f.close()

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
knn = joblib.load('distance_index/filename.pkl')
#joblib.dump(y1, 'F:/medical_result/y1/filename.pkl')
y1 = joblib.load('y1/filename.pkl')
distance_index=knn.kneighbors(X1, 5, return_distance=True)
#print "distance_index:",distance_index
f2=open("F:/medical_result/label_y.txt")
label=[]
result_1=[];result_2=[];result_3=[];result_4=[];result_5=[]
for li in f2.readlines():
    li=li.split()[0]
    label.append(li)
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

# print "result_1:",result_1
# print "result_2:",result_2
# print "result_3:",result_3
# print "result_4:",result_4
# print "result_5:",result_5


"西药（A）:"
medical0=[]
clf0 = joblib.load('medical_A/filename.pkl')
prediction0 = clf0.predict(X)
prediction0=prediction0.toarray()[0]
f0=open('label_A.txt','r')
label_A=[]
for li in f0.readlines():
    label_A.append(li.strip())
for i,li in enumerate(prediction0):
    if li!=0:
        medical0.append(label_A[i])
f0.close()

"中成药（B）:"
medical1=[]
clf1 = joblib.load('medical_B/filename.pkl')
prediction1 = clf1.predict(X)
prediction1=prediction1.toarray()[0]
f1=open('label_B.txt','r')
label_B=[]
for li in f1.readlines():
    label_B.append(li.strip())
for i,li in enumerate(prediction1):
    if li!=0:
        medical1.append(label_B[i])
f1.close()

"中草药（C）:"
medical2=[]
clf2 = joblib.load('medical_C/filename.pkl')
prediction2 = clf2.predict(X)
prediction2=prediction2.toarray()[0]
f2=open('label_C.txt','r')
label_C=[]
for li in f2.readlines():
    label_C.append(li.strip())
for i,li in enumerate(prediction2):
    if li!=0:
        medical2.append(label_C[i])
f2.close()

"检验（D）:"
medical3=[]
clf3 = joblib.load('medical_D/filename.pkl')
prediction3 = clf3.predict(X)
prediction3=prediction3.toarray()[0]
f3=open('label_D.txt','r')
label_D=[]
for li in f3.readlines():
    label_D.append(li.strip())
for i,li in enumerate(prediction3):
    if li!=0:
        medical3.append(label_D[i])
f3.close()

"检查（E）:"
medical4=[]
clf4 = joblib.load('medical_E/filename.pkl')
prediction4 = clf4.predict(X)
prediction4=prediction4.toarray()[0]
f4=open('label_E.txt','r')
label_E=[]
for li in f4.readlines():
    label_E.append(li.strip())
for i,li in enumerate(prediction4):
    if li!=0:
        medical4.append(label_E[i])
f4.close()

"疗效:"
clf8 = joblib.load('cure_after/filename2.pkl')
predictions = list(clf8.predict(X).toarray()[0])
if 1 in predictions:
    cure_after=predictions.index(1)
else:
    #cure_after=random.randint(4,8)
    cure_after=5

"""使用关联技术对疾病进行分析"""
medical5=[]
feature1_index=[]
X_index=[]
f5=open("feature1.txt","r")
for li in f5.readlines():
    feature1_index.append(li.strip())
f5.close()

for li in sorted(diag):
    #X_index.append(str(feature1_index.index(li)))
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
f6=open("result_x_0.7.txt","r")
index_dict={}
for li in f6.readlines():
    li=li.split("--->")
    index_dict[li[0]]={}
    index_dict[li[0]]["X"]=li[1]
    index_dict[li[0]]["y"]=li[2].strip()
f6.close()
#print "index_dict:",index_dict

refer_to={}
for li in prob_result:
    if li not in index_dict.keys():
        continue
    else:
        value=index_dict[li]
        refer_to[value["y"]]=value["X"]

refer_to_sorted = sorted(refer_to.items(), key=lambda x: x[0], reverse=True)
k=3
if len(refer_to_sorted)==0:
    pass
elif len(refer_to_sorted)>0 and len(refer_to_sorted)<k:
    for i in range(len(refer_to_sorted)):
        medical5.append(refer_to_sorted[i])
else:
    for i in range(k):
        medical5.append(refer_to_sorted[i])

#相关数据的输出
# print "西药（A）:",medical0
# print "中成药（B）:",medical1
# print "中草药（C）:",medical2
# print "检验（D）:",medical3
# print "检查（E）:",medical4
# print "与之相关的疾病有:",medical5
# print "疗效：",'5'#cure_after

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

print "与之相关的疾病有:",medical5



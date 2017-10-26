#!usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import codecs
from numpy import *
import Apriori
from sklearn.externals import joblib

f=open("F:/test/medical/case_diag.csv","r")
content=csv.reader(f)
data={}
for i,row in enumerate(content):
    if i==0:
        continue
    else:
        if row[1] not in data.keys():
            data[row[1]]=[]
            data[row[1]].append(row[3])
        else:
            data[row[1]].append(row[3])

feature=[]
for li in data.keys():
    content=sorted(data[li])
    if len(content)!=0:
        feature.append(content)

dataSet=feature
c1=Apriori.createC1(dataSet)
print "dataset:",dataSet
print "c1:",c1
L,suppData=Apriori.apriori(dataSet,minSupport = 0.001)
rules=Apriori.generateRules(L,suppData,minConf=0.30)
print "L:",L
print "suppData:",suppData
print "rules:",rules
f=open("date/result_sorted_0.3.txt","w")
for li in rules:
    for i,lj in enumerate(sorted(list(li[0]))):
        #print "i,lj",i,lj
        if (i+1)!=len(list(li[0])):
            f.write(str(lj)+",")
        else:
            f.write(str(lj))
    f.write("--->")
    for i,lj in enumerate(sorted(list(li[1]))):
        if (i+1)!=len(list(li[1])):
            f.write(str(lj)+",")
        else:
            f.write(str(lj))
    f.write("--->")
    f.write(str(li[2])+"\n")
f.close()

"""找出概率最大的几个事件,"""
f6=open("date/result_sorted_0.3.txt","r")
index_dict={}
for li in f6.readlines():
    li=li.split("--->")
    if li[0] not in index_dict.keys():
        index_dict[li[0]]=[]
    index_dict[li[0]].append((li[1],li[2].strip()))
    index_dict[li[0]]=sorted(index_dict[li[0]], key=lambda x: x[1], reverse=True)
f6.close()
joblib.dump(index_dict,"F:/medical_result/apriori_analysis_dict.pkl")
index_dict=joblib.load("F:/medical_result/apriori_analysis_dict.pkl")

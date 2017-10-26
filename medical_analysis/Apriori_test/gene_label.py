#!usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import codecs

# f2=open("label.txt","w")
# f=open("F:/test/case_diag.csv","r")
# content=csv.reader(f)
# feature=[]
# for i,li in enumerate(content):
#     if i!=0:
#         feature.append(li[3])
# print(len(set(feature)))
#
# f1=open("F:/test/prescribe_record.csv","r")
# content1=csv.reader(f1)
# label=[]
# for i,row in enumerate(content1):
#     if i!=0:
#         label.append(row[8])
# print(len(set(label)))
#
# for li in sorted(set(feature)):
#     f2.write('@attribute '+li+" {0,1}"+"\n")
# for li in sorted(set(label)):
#     f2.write('@attribute '+"TAG_"+li+" {0,1}"+"\n")


f2=open("label_y.txt","w")
f=open("F:/test/case_diag.csv","r")
content=csv.reader(f)
feature=[]
for i,li in enumerate(content):
    if i!=0:
        feature.append(li[3])
print(len(set(feature)))

f1=open("F:/test/prescribe_record.csv","r")
content1=csv.reader(f1)
label=[]
for i,row in enumerate(content1):
    if i!=0:
        label.append(row[8])
print(len(set(label)))

for li in sorted(set(label)):
    f2.write(li+"\n")

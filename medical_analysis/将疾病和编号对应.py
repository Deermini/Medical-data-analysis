# !usr/bin/env python
# -*- coding:utf-8 -*-
import csv
from sklearn.externals import joblib

f=open("F:/test/medical/case_diag.csv","r")
content=csv.reader(f)
diag_to_chinese_dict={}
label='ooo'
for li in content:
    if li[3]!=label and li[3] not in diag_to_chinese_dict.keys():
        label=li[3]
        diag_to_chinese_dict[li[3]]=li[5]

joblib.dump(diag_to_chinese_dict, 'F:/medical_result/diag_to_chinese_dict.pkl')
diag_to_chinese_dict2 = joblib.load('F:/medical_result/diag_to_chinese_dict.pkl')

print(diag_to_chinese_dict2['A04.900'])


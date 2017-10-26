#!usr/bin/env python
# -*- coding:utf-8 -*-

f=open("feature0.txt","r")
index_x=[]
for li in f.readlines():
    li=li.strip()
    index_x.append(li)
#print index_x

f2=open("result_x_0.5.txt","w")
f3=open("result_sorted_0.5.txt","r")
for li in f3.readlines():
    li=li.strip().split("--->")
    print "li:",li
    for j,i in enumerate(li[0].split(",")):
        str_x = str(index_x[int(i)])
        if (j+1)!=len(li[0].split(",")):
            f2.write(str_x+',')
        else:
            f2.write(str_x)
    f2.write("--->")
    for j,i in enumerate(li[1].split(",")):
        str_x = str(index_x[int(i)])
        if (j+1)!=len(li[1].split(",")):
            f2.write(str_x+',')
        else:
            f2.write(str_x)
    f2.write("--->")
    f2.write(str(li[2])+"\n")



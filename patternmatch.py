# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:45:19 2017

@author: RAHUL
"""

pattern='bob'
count =0
flag=True
start=0
a=0
while flag:
    a = s.find(pattern,start)  
                                  
    if a==-1:         
        flag=False
    else:
        count+=1
        start=a+1
print(count)
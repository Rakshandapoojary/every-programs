# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:25:35 2022

@author: Admin
"""

%%time
#Used to calculate total operation time
list1 = list(range(1,1000000))
list2 = list(range(2,1000001))
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
    
%%time
#Used to calculate total operation time
#Importing Numpy
import numpy as np
#Creating a numpy array of 1 million numbers
a = np.arange(1,1000000)
b = np.arange(2,1000001)
c = a+b

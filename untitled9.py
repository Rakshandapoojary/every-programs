# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:09:19 2022

@author: Admin
"""

import numpy as np
import pandas as pd
marks=pd.DataFrame({'Student_name':['Gruthi','Shreya','Lakshmitha','Shivani'],
                   'M1':[50,35,70,100],
                   'M2':[60,60,80,78],
                   'M3':[80,90,23,15],
                   'M4':[90,20,35,90]})
marks['Total']=marks['M1']+marks['M2']+marks['M3']+marks['M4']
f=marks['M1']<35
marks.mask(f,'Fail')
print(marks)
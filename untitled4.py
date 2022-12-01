# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:20:18 2022

@author: Admin
"""

import pandas as pd
marks=pd.DataFrame({'student_name':['gruthi','shreya','lakshmitha','shivani'],
                    'M1':[50,35,70,100],
                    'M2':[60,60,80,78],
                    'M3':[80,90,23,15],
                    'M4':[90,20,35,90]})
marks['Total']=marks['M1']+marks['M2']+marks['M3']+marks['M4']
marks['result']=(marks['M1']<35)+(marks['M2']<35)+(marks['M3']<35)+(marks['M4']<35)
pd_dict={True:'Fail',False:'Pass'}
marks['result']=marks['result'].replace(pd_dict)
print
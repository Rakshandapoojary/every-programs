# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:09:25 2022

@author: Admin
"""

import numpy as np
#creating a list of lists of 5 mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#creating a numpy array from attributes list
car_attributes_arr = np.array(car_attributes)
print(car_attributes_arr.dtype)

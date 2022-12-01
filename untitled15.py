# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:46:42 2022

@author: Admin
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
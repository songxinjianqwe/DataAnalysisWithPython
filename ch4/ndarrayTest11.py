# coding=utf-8
import numpy as np;
cond1 = [True,True,False,True,False];
cond2 = [False,False,True,True,False];
arr = np.where(cond1 and cond2,0, np.where(cond1, 1,np.where(cond2,2,3)));
print(arr);
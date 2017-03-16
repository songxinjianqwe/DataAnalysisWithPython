#coding=utf-8
import numpy as np;
arr = np.random.randn(100);
# 布尔值会被强制转为1和0
print((arr > 0).sum());
bools = np.array([False,False,True,False]);
print(bools.any());
print(bools.all());



#coding=utf-8
import numpy as np;

samples = np.random.normal(size=(4,4));
print(samples);

arr = [23,3,2,6,22,97,6,5,5,34,52,35,63,236,3,42];
np.random.shuffle(arr);
print(arr);
print(np.random.randint(2,5));

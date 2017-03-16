import numpy as np;

arr2D = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]]);
print(arr2D[:2]);
print(arr2D[:2,1:]);
print(arr2D[1,:2]);
print(arr2D[2,:1]);
print();
print(arr2D[:,:1]);
#:表示全选

arr2D[:2,1:] = 0;
print(arr2D);


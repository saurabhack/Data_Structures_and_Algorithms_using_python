import numpy as np
firstArray=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print("first array is ==",firstArray)
addFirstArray=np.insert(firstArray,5,[[1,2,3]],axis=1)
print("first array is == ",addFirstArray)
secondTwoArray=np.insert(firstArray,3,[[11,12,13,14,15]],axis=0)
print("second array is == ",secondTwoArray)



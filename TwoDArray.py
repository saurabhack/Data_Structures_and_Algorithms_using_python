import numpy as np
firstArray=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print("first array is ==",firstArray)
addFirstArray=np.insert(firstArray,5,[[1,2,3]],axis=1)
print("first array is == ",addFirstArray)
secondTwoArray=np.insert(firstArray,3,[[11,12,13,14,15]],axis=0)
print("second array is == ",secondTwoArray)


#accessing the element from two dimensional array in python
# accessing entire column of the two dimensional array 
print("first row of the array === ",firstArray[:,1])
#accessing single element of the two dimensional array
print("second element of the third line of the array == ",firstArray[2][1])
#accessing entire single line or row in two dimensional array 
print("entire second line of the row is == ",firstArray[1])

# traversing Using array is 

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=" ")
        print("\n")

traverseTDArray(firstArray)
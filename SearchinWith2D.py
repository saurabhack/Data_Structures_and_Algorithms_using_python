#two dimensional array linear searching 
import numpy as np

firstArray=np.array([[11,15,10,6],[12,17,12,8],[15,18,14,9]])


def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if(array[i][j]==value):
                return "the value is located at the index of "+str(i)+" "+str(j)
            
    return "the element is not found"

print(searchTDArray(firstArray,18))

# time complexity = O(mn)
# space complexity = O(1)
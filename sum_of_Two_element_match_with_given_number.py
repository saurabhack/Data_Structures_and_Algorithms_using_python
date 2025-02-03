def findNumber(arr,number):
    leftToRight=0
    rightToLeft=len(arr)-1
    while(leftToRight!=rightToLeft):
        if(arr[leftToRight]+arr[rightToLeft]<number):
            leftToRight=leftToRight+1
        elif(arr[leftToRight]+arr[rightToLeft]>number):
            rightToLeft=rightToLeft+1
        elif(arr[leftToRight]+arr[rightToLeft]==number):
            return [arr[rightToLeft],arr[leftToRight]]
    return -1


print("number is found == ",findNumber([1,2,3,4,5],9))

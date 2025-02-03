#missing number
#first approach
first=[1,2,3,4,6]
print(first)
def missing_number(arr,size):
    ans=0
    for i in range(len(arr)-1):
        print("first==",arr[i])
        print("second==",arr[i+1])
        if(arr[i]-arr[i+1]!=-1 and arr[i]-arr[i+1]==-2):
            ans=arr[i]+1
    return ans
print(missing_number(first,6))

#second Approach


def missing_number2(arr,size):
    size=size*(size+1)//2
    print("size==",size)
    addition=sum(arr)
    print("total addition of the code is == ",addition)
    missing=size-addition
    print("missing number == ",missing)
    return missing

missing_number2(first,6)




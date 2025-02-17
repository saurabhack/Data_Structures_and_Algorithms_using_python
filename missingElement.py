#find missing element
def total(arr):
    return sum(arr)
def searching(arr,key):
    for i in arr:
        if i==key:
            return True
    return False
def findMissing(arr):
    first=arr[0]
    last=arr[len(arr)-1]
    totalLength=(first+last)-1
    addition=(totalLength*(totalLength+1))//2
    missing=addition-sum(arr)
    data=arr
    ans=[]
    while missing!=0:
        if searching(arr,missing):
            missing-=1
        else:
            data.append(missing)
            if total(data)==addition and missing < last:
                ans.append(missing)
                print("the why element is inserted in this lists == ",ans)
                break
            else:
                if(missing<last):    
                    ans.append(missing)
                    missing-=1
    return ans
arr=[1,3,5]
print("answer and output is ===> ",findMissing(arr))
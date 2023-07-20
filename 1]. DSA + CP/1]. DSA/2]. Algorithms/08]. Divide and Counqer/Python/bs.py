def binarysearch(n,arr):
    #logic 
    low=0
    high=len(arr)-1 #or len(arr) but -1 is better
    if low==high: #if only one element
        if arr[low]==n:
            return low
        else: #if no element
            return -1

    while(low<=high):
        mid=(low+(high-low)//2)
        if arr[mid]==n:
            return mid
        elif arr[mid]<n:
            low=mid+1
        else:
            high=mid-1
    return -1 #esc case as element not found
#logic ends
n=10
arr=[]
print(binarysearch(n,arr))
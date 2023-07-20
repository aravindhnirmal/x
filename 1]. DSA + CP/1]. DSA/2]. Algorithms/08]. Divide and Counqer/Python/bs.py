def binarysearch(n,arr):
    #logic 
    low=0
    high=len(arr)-1 #or len(arr) but -1 is better
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
arr=[0,1,2,3,4,5,6,7,8,9,10]
print(binarysearch(n,arr))
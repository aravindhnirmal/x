def search(arr,elt):
    for index in range(0,len(arr)):
        if arr[index]==elt:
            return index
        

arr=[1,2,3,4,5]
elt=3
print("Before Search:",arr)
print("Element to search:",elt)
print("After Search:",search(arr,elt))

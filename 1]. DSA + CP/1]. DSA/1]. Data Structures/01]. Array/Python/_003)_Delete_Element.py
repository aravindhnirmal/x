"""
two questions generate  to delete an element from a list
1. [3,2,2,3] [3,2,2,_] delete the index as given by user
2.[3,2,3,2] [2,2,_,_] delete the duplicate element as given by user
"""
# # first method to delete an element from a list as pop use or remove use
# def delete(arr,index):
#     print("Before Delete:",arr)
#     arr.pop(index)
#     print("After Delete:",arr)

# arr=[1,2,3,4,5]
# index=int(input("Enter the index to delete:"))
# delete(arr,index)
    



# second method is delete the duplicate element from a list
def delete_duplicate(arr,elt): #two or three method use in this program
    #in the delete duplicate element we use the while loop
    while elt in arr:
        arr.remove(elt)
    print("After Delete:",arr)
#in this program we use the while and iteration i 
    # i=0
    # while i<len(arr):
    #     if arr[i]==elt:
    #         arr.pop(i)
    #     else:
    #         i+=1

    # print("After Delete:",arr)



arr=[1,1,23,23,2]
ele=int(input("Enter the number to delete:"))
delete_duplicate(arr,ele)
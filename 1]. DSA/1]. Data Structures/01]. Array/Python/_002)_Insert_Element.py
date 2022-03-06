"""
Function to insert a new element at a given position

Takes the position of an array and an element as arguments
"""


def insert(arr, index, successor):
    
    for index in range(index, len(arr)):
        arr[index], successor = successor, arr[index]

    arr.append(successor)
    

arr = [1, 2, 3, 5]
print("Array before insertion:", arr)

insert(arr, 1, -4)
print("Array after insertion:", arr)

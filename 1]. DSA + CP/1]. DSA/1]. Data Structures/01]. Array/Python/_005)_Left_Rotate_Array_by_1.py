"""
Function to rotate an the first element
"""


def left_rotate(arr, num):
 #METHOD 1
      for index in range(num):
        arr.append(arr.pop(0)) #revisit this line
        #append means add the element in the last of the list
        #pop means delete the element from the list
    #METHOD 2 . # arr[1: ]+arr[0:1] #means 1 to last element + 0 to 1 element
       
arr = [1, 2, 3, 4, 5]
num = 2

print("Before Left Rotation:", arr)

left_rotate(arr, num)
print("After '1' Left Rotation:", arr)

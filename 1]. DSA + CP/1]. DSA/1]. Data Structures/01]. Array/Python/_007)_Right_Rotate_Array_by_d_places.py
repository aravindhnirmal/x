arr = [1, 2, 3, 4, 5]
num = 2

# Performing right rotation on the array
arr[:] =  arr[-num:]+arr[:-num] 
#-num means from the last element to num-1 element
#arr[-num:] means from the last element to num-1 element
#arr[:num] means 0 to num-1 element
#arr[:] means the whole array

print(arr)  # Output: [4, 5, 1, 2, 3]

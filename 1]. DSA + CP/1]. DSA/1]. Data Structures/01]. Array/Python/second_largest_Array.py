# def second_large_num(arr):
       
    # num=arr
    # num.reverse()
    # return num[1]
#or 
def find_second_largest_with_index(arr):
    num = list(set(arr))
    num.sort(reverse=True)
    second_largest = num[1]
    index = arr.index(second_largest)
    return second_largest, index

# Example usage:
arr = [10, 5, 8, 15, 12]
second_largest, index = find_second_largest_with_index(arr)
print("Second largest number:", second_largest) 
print("Index of second largest number:", index)  

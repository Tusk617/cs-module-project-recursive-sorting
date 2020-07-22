# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start < end:
        #declaring our midpoint
        mid = (start + end) // 2
        #checking if our midpoint is the target value
        #if it is, then just return the midpoint
        if target == arr[mid]:
            return mid
        #else, we need to see if our target is less than or 
        #greater than the midpoint, so we know what direction
        #to continue in
        if target < arr[mid]:
            return binary_search(arr, target, start, end - 1)
        elif target > arr[mid]:
            return binary_search(arr, target, start + 1, end)
    #if start and end are the same index, then the target value
    #probably isnt in the the array. So just return -1
    else:
        return -1



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here


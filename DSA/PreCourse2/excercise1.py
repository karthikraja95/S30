# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, left, right, x):

    # write your code here
    mid = 0
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1

        elif arr[mid] > x:
            right = mid - 1

        else:
            return mid

    # If the element is not present in the array, return -1
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

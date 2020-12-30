# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):

    """
    Algorithm:
    1. Compare x with the middle element.
    2. If x matches with the middle element, we return the mid index.
    3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element.
        Then we apply the algorithm again for the right half.
    4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
    """
    # write your code here
    mid = 0
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] < x:
            l = mid + 1

        elif arr[mid] > x:
            r = mid - 1

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

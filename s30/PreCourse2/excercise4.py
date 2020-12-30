# Python program for implementation of MergeSort
def mergeSort(arr):

    # write your code here

    # Checking wheather the array is empty or not
    if len(arr) > 1:
        # Find mid of the array
        mid = len(arr) // 2

        # Divide the array into two halves L and R
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the Left half
        mergeSort(L)
        # Sorting the Right half
        mergeSort(R)

        # Now the actual algorithm starts
        i = j = k = 0

        # Copy the data to two temp arrays L and R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i + 1

            else:
                arr[k] = R[j]
                j = j + 1

            k = k + 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1


# Code to print the list
def printList(arr):

    # write your code here
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

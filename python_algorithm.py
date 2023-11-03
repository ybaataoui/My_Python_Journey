# Palindrome Algorithm
def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True
# Test cases
print(isPalindrome("racecar")) # Should print true

#Big O Notation

# O(1) - Constant Time
# In algorithms with constant time complexity, the runtime does not depend on the size of the input data. It remains constant, making it the most efficient scenario.
# Example: Accessing an element in an array by its index.

def access_element(arr, index):
    return arr[index]

# No matter how large the array is, accessing an element by its index takes the same amount of time. The runtime is constant, and we denote it as O(1).


# O(n) - Linear Time
# Algorithms with linear time complexity have a runtime that grows linearly with the size of the input data. This means that if the input data doubles in size, the runtime also doubles.
# Example: Searching for a specific value in an unsorted list.

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False
# As the size of the list (arr) increases, the number of iterations the loop performs also increases linearly. Therefore, this algorithm has a time complexity of O(n).

# O(n^2) - Quadratic Time
# Algorithms with quadratic time complexity have runtimes that grow with the square of the input size. As the input data size increases, the runtime increases quadratically.
# Example: Bubble Sort, a simple sorting algorithm.
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Bubble sort has a time complexity of O(n^2). As the size of the input list (arr) increases, the number of comparisons and swaps grows quadratically.

# O(log n) - Logarithmic Time
# Algorithms with logarithmic time complexity have runtimes that grow logarithmically with the size of the input data. Logarithmic time complexity is considered very efficient.
# Example: Binary search in a sorted list.
def binarySearch(arr, target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
#Binary search drastically reduces the search time as the size of the sorted list (arr) grows. It has a time complexity of O(log n)


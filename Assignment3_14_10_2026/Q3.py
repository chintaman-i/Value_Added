"""
Check if the Array is Sorted
Example 1:
Input:
n = 5
arr = [1, 2, 3, 4, 5]
Output:
True
Explanation: The given array is sorted; every element in the array is smaller than or equals to its next value. Therefore, the answer is True.
Example 2:
Input:
n = 5
arr = [5, 4, 6, 7, 8]
Output:
False
Explanation: The given array is not sorted; element 5 is not smaller than or equal to its next value 4. Therefore, the answer is False.
Example 1:
Input: {"arr": [1, 2, 3, 4, 5]}
Output: true
Example 2:
Input: {"arr": [5, 4, 6, 7, 8]}
Output: false """

#Solution
def isArraySorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
    
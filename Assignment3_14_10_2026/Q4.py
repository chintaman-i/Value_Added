""" Reverse an Array In-Place
Examples
Example 1:
Input:
{"n": 5, "arr": [1, 2, 3, 4, 5]}
Output:
[5, 4, 3, 2, 1]
Explanation: The reverse of the array [1, 2, 3, 4, 5] is [5, 4, 3, 2, 1].
Example 2:
Input:
{"n": 6, "arr": [1, 2, 1, 1, 5, 1]}
Output:
[1, 5, 1, 1, 2, 1]
Explanation: The reverse of the array [1, 2, 1, 1, 5, 1] is [1, 5, 1, 1, 2, 1].
Example 1:
Input: {"arr": [1, 2, 3, 4, 5]}
Output: [5, 4, 3, 2, 1]
Example 2:
Input: { "arr": [1, 2, 1, 1, 5, 1]}
Output: [1, 5, 1, 1, 2, 1]
"""

#Solution

def reverseArray(arr):
    for i in range(len(arr)):
        return arr[::-1]

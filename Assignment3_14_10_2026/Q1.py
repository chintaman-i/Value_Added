""" Sum of Array Elements
Example 1: Input:
{"n": 5, "arr": [1, 2, 3, 4, 5]}
Output:
15
Explanation: The sum of all the elements is 1 + 2 + 3 + 4 + 5 = 15.
Example 2: Input:
{"n": 6, "arr": [1, 2, 1, 1, 5, 1]}
Output:
11
Explanation: The sum of all the elements is 1 + 2 + 1 + 1 + 5 + 1 = 11.
Example 1:
Input: {"n": 5, "arr": [1, 2, 3, 4, 5]}
Output: 15
Example 2:
Input: {"n": 6, "arr": [1, 2, 1, 1, 5, 1]}
Output: 11

"""

#solution
def sum_of_array_elements(n, arr):
    if n<0:
        return False
        
    sum=0
    for i in arr:
        sum+=i
    
    return sum


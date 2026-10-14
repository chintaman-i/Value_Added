""" Count of Odd Numbers in Array
Input: n=5, array = [1,2,3,4,5]
Output: 3
Explanation: The three odd elements are (1, 3, 5).
Example 2:
Input: n=6, array = [1,2,1,1,5,1]
Output: 5
Explanation: The five odd elements are one 5 and four 1's.
Input: n=5, array = [1,3,5,7,9]
Examples
Example 1:
Input: {"n": 5, "array": [1, 2, 3, 4, 5]}
Output: 3
Example 2:
Input: {"n": 6, "array": [1, 2, 1, 1, 5, 1]}
Output: 5
 """
#solution

def countOddNumbers(n, array):
    count=0
    for i in array:
        if i%2!=0:
            count+=1
    
    return count 

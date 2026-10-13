""" Find Divisors of a Number
You are given an integer n. Your task is to find all the divisors of n and return them in a sorted array.
A number which completely divides another number is called its divisor.
Example 1:
Input: n = 6
Output: [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, and 6.
Example 2:
Input: n = 8
Output: [1, 2, 4, 8]
Explanation: The divisors of 8 are 1, 2, 4, and 8.
Examples
Example 1:
Input: {"n": 6}
Output: [1, 2, 3, 6]
Example 2:
Input: {"n": 8}
Output: [1, 2, 4, 8]
 """

#Solution
def findDivisors(n):
    result=[]
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)

    return result

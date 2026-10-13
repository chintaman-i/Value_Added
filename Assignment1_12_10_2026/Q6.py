""" Digit in a number
Factorial of a Given Number
You are given an integer n. Return the value of n! (n factorial). The factorial of a number is the product of all positive integers less than or equal to that number.

Example 1:
Input:
{"n": 2}
Output:
2
Explanation: 2! = 1 * 2 = 2.
Example 2:
Input:
{"n": 0}
Output:
1
Explanation: 0! is defined as 1.
Example 1:
Input: {"n": 2}
Output: 2
Explanation: Sample testcase example
Example 2:
Input: {"n": 0}
Output: 1 """

#solution

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i

    return fact
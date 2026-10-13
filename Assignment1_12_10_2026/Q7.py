""" Check if the Number is Armstrong
Easy
Arrays & Hashing
Module: ASSIGNMENT
You are given an integer n. You need to check whether it is an Armstrong number or not.
Return true if it is an Armstrong number, otherwise return false.
An Armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.
Examples
Example 1:

Input: n = 153

Output: true

Explanation: Number of digits : 3.

1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

Therefore, it is an Armstrong number.

Example 2:

Input: n = 12

Output: false

Explanation: Number of digits : 2.

1^2 + 2^2 = 1 + 4 = 5.

Therefore, it is not an Armstrong number.

Examples
Example 1:
Input: {"n": 153}
Output: true
Example 2:
Input: {"n": 12}
Output: false
"""

#solution

def isArmstrong(n):
    amstrong=0
    original=n
    count=len(str(n))

    if n==0:
        return True
    while n>0:
        digit=n%10
        amstrong+=digit**count
        n=n//10

    return original==amstrong
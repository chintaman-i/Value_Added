""" Reverse an Integer
You are given an integer n. Your task is to return the integer formed by placing the digits of n in reverse order.
Note that the result should not have leading zeros.
Example 1:
Input: n = 25
Output: 52
Explanation: The reverse of 25 is 52.
Example 2:
Input: n = 123
Output: 321
Explanation: The reverse of 123 is 321.
Example 1:
Input: {"n": 25}
Output: 52

Example 2:
Input: {"n": 123}
Output: 321 """

#solution

def reverseInteger(n):
    rev_no=0
    sign=-1 if n<0 else 1
    n=abs(n)
    
    while n > 0:
        digit=n%10
        rev_no=rev_no*10+digit
        n=n//10
    
    return sign*rev_no
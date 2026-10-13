""" Palindrome Number
You are given an integer n. Your task is to determine if n is a palindrome number.
A palindrome number is one that reads the same when reversed.
Example 1:
Input: n = 121
Output: true
Explanation: When read from left to right: 121. When read from right to left: 121.
Example 2:
Input: n = 123
Output: false
Explanation: When read from left to right: 123. When read from right to left: 321.
Example 1:
Input: {"n": 121}
Output: true

Example 2:
Input: {"n": 123}
Output: false """

#solution

def isPalindrome(n):
    original=n
    rev_no=0
    while n >0:
        digits=n%10
        rev_no=rev_no*10+digits
        n=n//10

    return original==rev_no
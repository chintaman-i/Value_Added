""" Count Odd Digits
You are given an integer n. Your task is to return the number of odd digits present in the number.
The number will have no leading zeroes, except when the number is 0 itself.
Example 1:
Input: n = 5
Output: 1
Explanation: 5 is an odd digit.
Example 2:
Input: n = 25
Output: 1
Explanation: The only odd digit in 25 is 5.
Example 1:
Input: {"n": 5}
Output: 1
Explanation: Sample testcase example
Example 2:
Input: {"n": 25}
Output: 1 """

#solution

def countOddDigits(n):
    count=0
    while n>0:
        digit=n%10

        if digit %2!=0:
            count+=1
        
        n=n//10
    
    return count

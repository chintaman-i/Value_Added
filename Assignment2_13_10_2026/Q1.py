""" Check for Perfect Number
Check for Perfect Number
You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.
A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.
Example 1
Input:
{"n": 6}
Output:
true
Explanation: Proper divisors of 6 are 1, 2, 3. 1 + 2 + 3 = 6.
Example 2
Input:
{"n": 4}
Output:
false
Explanation: Proper divisors of 4 are 1, 2. 1 + 2 = 3.
Examples
Example 1:
Input: {"n": 6}
Output: true
Example 2:
Input: {"n": 4}
Output: false
"""

#solution
def isPerfectNumber(n):
    sqr=int(n**0.5)
    sum=1
    for i in range(1,sqr+1):
        if n%i==0:
            sum+=1
            if n!=n//i:
                sum+=n//i
    return sum

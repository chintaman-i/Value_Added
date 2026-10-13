""" Check for Prime Number
You are given an integer n. Your task is to check if the number is prime or not.
A prime number is defined as a number greater than 1 that has no divisors other than 1 and itself.
Example 1:
Input: n = 5
Output: true
Explanation: The only divisors of 5 are 1 and 5, so the number 5 is prime.
Example 2:
Input: n = 8
Output: false
Explanation: The divisors of 8 are 1, 2, 4, and 8, thus it is not a prime number.
example 1:
Input: {"n": 5}
Output: true
Example 2:
Input: {"n": 8}
Output: false
 """
#solution

def is_prime(n):
    if n < 2:
        return False
    sqr=(n**0.5)
    for i in range(2, sqr + 1):
        if n % i == 0:
            return False
    return True

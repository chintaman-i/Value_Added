"""Return the Largest Digit in a Number
You are given an integer n. Your task is to return the largest digit present in the number.

Example 1:
Input:
{"n": 25}
Output:
5
Explanation: The largest digit in 25 is 5.
Example 2:
Input:
{"n": 99}
Output:
9
Explanation: The largest digit in 99 is 9.

Example 1:
Input: {"n": 25}
Output: 5
Explanation: Sample testcase example
Example 2:
Input: {"n": 99}
Output: 9
Explanation: Sample testcase example """

#solution

def returnLargestDigit(n):
    largest=0
    while n>0:
        digit=n%10
        if digit>largest:
            largest=digit
        n=n//10
    return largest
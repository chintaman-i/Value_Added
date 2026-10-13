""" Digit in a number
Count all Digits of a Number You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.
Example 1: Input: n = 4
Output: 1
Explanation: There is only 1 digit in 4.
Example 2: Input: n = 14
Output: 2
Explanation: There are 2 digits in 14.
Examples
Example 1:
Input: 12345
Output: 5
Explanation: Sample testcase example """

#solution

class Solution:
    def digitCounts(self, n: int) -> int:
        return len(str(n))
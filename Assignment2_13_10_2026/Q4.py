""" GCD of Two Numbers
You are given two integers n1 and n2. Your task is to find the Greatest Common Divisor (GCD) of the two given numbers.
The GCD of two integers is the largest positive integer that divides both of the integers without leaving a remainder.
Examples:
Example 1:
Input:
{"n1": 4, "n2": 6} 
Output:
2 
Explanation: Divisors of n1 = 1, 2, 4; Divisors of n2 = 1, 2, 3, 6;
Greatest Common divisor = 2.
Example 2:
Input:
{"n1": 9, "n2": 8} 
Output:
1 
Explanation: Divisors of n1 = 1, 3, 9; Divisors of n2 = 1, 2, 4, 8;
Greatest Common divisor = 1.
Examples
Example 1:
Input: {"n1": 4, "n2": 6}
Output: 2
Example 2:
Input: {"n1": 9, "n2": 8}
Output: 1 """

#Solution
def gcdOfTwoNumbers(n1, n2):
    list1=[]
    list2=[]
    common=[]

    for i in range(1,n1+1):
        if n1%i==0:
            list1.append(i)

    for i in range(1,n2+1):
        if n2%i==0:
            list2.append(i)

    for i in list1:
        if i in list2:
            common.append(i)
            
    return max(common)

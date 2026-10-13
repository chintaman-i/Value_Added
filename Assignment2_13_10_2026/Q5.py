""" Lowest Common Multiple (LCM) of Two Numbers
You are given two integers n1 and n2. Your task is to find the Lowest Common Multiple (LCM) of the two given numbers.
The LCM of two integers is the smallest positive integer that is divisible by both integers.
Example 1:
Input:
n1 = 4, n2 = 6
Output:
12
Explanation:
4 * 3 = 12, 6 * 2 = 12.
12 is the lowest integer that is divisible by both 4 and 6.
Example 2:
Input:
n1 = 3, n2 = 5
Output:
15
Explanation:
3 * 5 = 15, 5 * 3 = 15.
15 is the lowest integer that is divisible by both 3 and 5.
Example 1:
Input: {"n1": 4, "n2": 6}
Output: 12
Example 2:
Input: {"n1": 3, "n2": 5}
Output: 15
 """

#Solution
def findLcm(n1, n2):
    list1=[]
    list2=[]
    common=[]

    for i in range(n1+1):
        if i%n1==0:
            list1.append(i)
    for i in range(n2+1):
        if 1%n2==0:
            list2.append(i)

    for i in list1:
        if i in list2:
            common.append(i)
            
    return min(common)
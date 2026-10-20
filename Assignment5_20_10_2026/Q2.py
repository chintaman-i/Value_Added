"""Longest Common Prefix
Given an array of strings str, find the longest common prefix shared by all
the strings in the array.

A prefix is a sequence of characters that appears at the beginning of a
string.

If there is no common prefix among all the strings, return an empty string

Example:
Example 1 :-
Input: str = ["flowers", "flow", "fly", "flight"]
Output: "fl"
Explanation: All strings start with "fl", but their next characters are
different. Therefore, the longest common prefix is "fl".

Example 2 :-
Input: str= ["dog", "cat", "animal", "monkey"]
Output:""
Explanation: No prefix is common to all the strings, so return an empty
string.

Example 1:

Input: {"str":["flowers", "flow", "fly", "flight"]}
Output: fl

Example 2:

Input: {"str":["dog","cat","animal","monkey"]}
Output: ""


Example 3:

Input: {"str":["lady","Lazy"]}
Output: la

 """
#solution

def longestCommonPrefix(str: list[str]) -> str:
    prefix=str[0]

    for s in str[1:]:
        i=0

        while i<len(prefix) and i<len(s):
            if s[i]==prefix[i]:
                i+=1
            else:
                break
        
        prefix=prefix[:i]

    return prefix

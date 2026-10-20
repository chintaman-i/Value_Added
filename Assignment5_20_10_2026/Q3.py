"""Isomorphic Strings
Given two strings s and t, determine whether they are isomorphic.

Two strings are isomorphic if every character in s can be replaced with a
character in t to make both strings identical, while preserving the order of
characters.

The mapping must follow these rules:

Each character in s must always map to the same character in t.
Two different characters in s cannot map to the same character in t.
A character can map to itself. Return true if the strings are isomorphic;
otherwise, return false.
Example 1:

Input: {"s":"egg","t":"add"}
Output: true

Example 2:

Input: {"s":"apple","t":"bbnbm"}
Output: false

Example 3:
Input: {"s":"paper","t":"title"}
Output: true


Example 4:

Input: {"s":"foo","t":"bar"}
Output: false """

#Solution
def isIsomorphic(s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False

    dictonary={}
    rev={}
    for i in range(len(s)):
        if s[i]  in dictonary:
            if dictonary[s[i]]!=t[i]:
                return False
        else:
                dictonary[s[i]]=t[i]

        if t[i] in rev:
            if rev[t[i]]!=s[i]:
                return False
        else:
                rev[t[i]]=s[i]
           

    return True

    
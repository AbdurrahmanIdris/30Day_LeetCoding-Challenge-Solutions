"""
Problem statement:
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted 
without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def solve(i,j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + solve(i+1,j+1)

            if text1[i] != text2[j]:
                return max(solve(i+1,j),solve(i,j+1))
        return solve(0,0)

##Not efficient for all cases or you can simply say it's wrong :'(((
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def longestSubsequence(string1: str, string2: str) -> int:
            subsequence_lengthes_list = []
            for index in range(len(string1)):
                i =  0
                temp = string2
                subsequence_length = 0
                for char in string1[index:]:
                    if char in temp:
                        i = min(temp.index(char) + 1, len(string2))
                        temp = temp[i:len(string2)]
                        subsequence_length += 1
                    subsequence_lengthes_list.append(subsequence_length)
            return max(subsequence_lengthes_list)
        return max(longestSubsequence(text1, text2),longestSubsequence(text2, text1))

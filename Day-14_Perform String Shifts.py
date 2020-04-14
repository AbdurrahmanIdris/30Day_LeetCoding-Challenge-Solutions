"""
Problem Statement:
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
#direction can be 0 (for left shift) or 1 (for right shift). 
#amount is the amount by which string s is to be shifted.
#A left shift by 1 means remove the first character of s and append it to the end.
#Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.
"""

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def rightShift(s: str) -> str:
            shifted = ""
            last_index = len(s) - 1
            shifted += s[last_index]
            for i in s[:last_index]:
                shifted += i
            return shifted        
        
        def leftShift(s: str) -> str:
            shifted = ""
            for i in s[1:]:
                shifted += i
            shifted += s[0]
            return shifted
        
        count = 0        
        for list_i in shift:
            if list_i[0] == 0:
                count -= list_i[1]
            else:
                count += list_i[1]

        res_s = s
        if count > 0:
            for i in range(count):
                res_s = rightShift(res_s)
        elif count < 0:
            for i in range(-count):
                res_s = leftShift(res_s)
                
        return res_s

"""
Problem statement:
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if 0 == m: return 0
        
        binary_m = "{0:b}".format(m)
        binary_n = "{0:b}".format(n)

        if len(binary_m) != len(binary_n): return 0
        
        result = m
        for i in range(m,n+1):
            result = result & i
        return result  

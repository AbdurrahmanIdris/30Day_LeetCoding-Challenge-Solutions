"""
Problem Statement:
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
"""
"""
Idea of the solution is that:
When a value of x repeated it means that the number of ones and zeros in that subarray are equal.
So when the code catch a repeat it calculates the length of this sub array and assigns it to the var. res.
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dicts = {}  #Dictionary holds each new value founded by x as a key.
        res = 0     #This is the final result variable.
        x = 0       # x denotes to the variable which updated with every repeat for to values of it.

        if len(nums) < 2 :
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] == 1:
                    x += 1
                else:
                    x -= 1

                if x == 0:    ##Special case because we start with x = 0.
                    res = i+1

                if x in dicts:
                    res = max(res,i-dicts[x])
                else:
                    dicts[x]=i
            return res

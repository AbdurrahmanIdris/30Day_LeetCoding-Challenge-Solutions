##I struggled solving this problem using python, I tried all approaches but I couldn't reach.
##Here's my tries using Python but all of them gives Time Limit Exceeded. So I tried same approaches using Java and it worked.
##You will find my Java solution here in this repository.

"""
Problem statement:
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
1.The length of the array is in range [1, 20,000].
2.The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

##Approach 1 (Cumulative sum)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = [0]
        output = 0
        
        for i in range(1,len(nums)+1):
            cumulative_sum.append(cumulative_sum[i-1] + nums[i-1])
        
        for i in range(len(cumulative_sum)):
            for j in range(i+1,len(cumulative_sum)):
                if (cumulative_sum[j] - cumulative_sum[i]) == k:
                    output += 1
                    
        return output
        
##Approach 2 (Brute Force)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum1 = 0
                for index in range(i,j):
                    sum1 += nums[index]
                    if sum1 == k:
                        output += 1
        return output

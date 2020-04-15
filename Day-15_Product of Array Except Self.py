"""
Problem Statement:
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to 
the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).
"""

#Accepted solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        length = len(nums)
        prefix = [0]*length
        suffix = [0]*length
        result = [0]*length
        
        #firstly, fill the prefix array. Note -> most left element = 1 becuase nothing in its left.
        prefix[0] = 1
        for i in range(1,length):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        #secondly, fill the suffix array. Note -> most right element = 1 becuase nothing in its right.
        suffix[length-1] = 1
        for i in range(length-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        #finally find the result product list
        for i in range(length):
            result[i] = prefix[i]*suffix[i]
        
        return result


#first try (Correct but Time Limit Exceeded error in one case out of 18 cases)
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        length = len(nums)
        result = [0]*length
        for i in range(length):
            product = 1
            for j in range(length):
                if j == i:
                    continue
                product *= nums[j]
            result[i] = product
        return result

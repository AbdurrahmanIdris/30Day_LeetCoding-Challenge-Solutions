"""
Problem statement:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

#BackTracking Approach (Failed: Time Limit Exceeded)
class SolutionBackTrack:
    def canJump(self, nums: List[int]) -> bool:
        def canJumpFromPos(pos,nums: List[int]):
            if pos == (len(nums)-1):
                return True
            furthest_step = min(pos + nums[pos],len(nums)-1)
            for i in range(pos+1,furthest_step+1):
                if(canJumpFromPos(i,nums)):
                    return True
            return False
        
        return canJumpFromPos(0,nums)
#Greedy Approach (Accepted)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if (i + nums[i] >= last_position):
                last_position = i
        return last_position == 0

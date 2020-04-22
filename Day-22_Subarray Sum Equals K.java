##Here's my solution in Java because Python solution gives Time Limit Exceeded.

/*
Problem statement:
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
1.The length of the array is in range [1, 20,000].
2.The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
*/
class Solution {
    public int subarraySum(int[] nums, int k) {
        int output = 0;
        int[] cumulative_sum = new int[nums.length + 1];
        cumulative_sum[0] = 0;
        for (int i = 1; i <= nums.length; i++)
            cumulative_sum[i] = cumulative_sum[i - 1] + nums[i - 1];
        for (int start = 0; start < nums.length; start++) {
            for (int end = start + 1; end <= nums.length; end++) {
                if (cumulative_sum[end] - cumulative_sum[start] == k)
                    output++;
            }
        }
        return output;
    }
}

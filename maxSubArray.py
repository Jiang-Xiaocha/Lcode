'''

Description:
41. 最大子数组

给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。
样例
给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6
要求时间复杂度为O(n)

Method:
采用贪心算法，如果子串的和已经为负数了，则丢弃重新计算。
采用方法一的时候因为担心全部为负数，就先用了max()函数找一个最大的，这样时间上就很慢，
其实只要像方法二一样变一下顺序就可以了，真是愚蠢的自己。

'''


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        temp = 0
        max_sum = max(nums)
        for i in range(0,len(nums)):
            temp = temp + nums[i]
            if (temp < 0):
                temp = 0
            if (temp > 0 and temp > max_sum):
                max_sum = temp
        return max_sum


# 更快
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        temp = 0
        max_sum = float('-inf')
        for i in range(0,len(nums)):
            temp = temp + nums[i]
            if(temp > max_sum):
                max_sum = temp
            if (temp < 0):
                temp = 0
        return max_sum





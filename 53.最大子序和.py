#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.94%)
# Likes:    1628
# Dislikes: 0
# Total Accepted:    161K
# Total Submissions: 327.2K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
# 思路1 dp 48ms 76%
# pre 就是dp[i-1] cur 就是dp[i]
# dp[i] = max(dp[i-1] + nums[i], nums[i]) 用pre处理dp
# ans更新答案
# 时间复杂度o(n)



# 思路2 分治法 时间复杂度O(n) 因为有额外空间 这题不如思路1
#       分治法的套路分为三步： 1. 定义基本情况 2. 将问题分解为子问题，并递归解决他们 3.合并子问题的解已获得原始问题的解。
# 这个算法比较复杂。 而且cross_num的定义有点绕。思路是要么在左半边，要么在右半边，要么穿过中间元素横跨两边
# 实际运行后超时。。。

# 当最大子数组有 n 个数字时：
# 若 n==1，返回此元素。
# left_sum 为最大子数组前 n/2 个元素，在索引为 (left + right) / 2 的元素属于左子数组。
# right_sum 为最大子数组的右子数组，为最后 n/2 的元素。
# cross_sum 是包含左右子数组且含索引 (left + right) / 2 的最大值。

# 引进了一个线段树的概念，在这个题里面发挥不太好但是这个数据结构能解决很多问题。


# @lc code=start
class Solution:
    # 思路1 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0 
        ans = nums[0] 
        for n in nums:            
            pre = max(n, pre + n)
            ans = max(pre, cur)
        
        return ans


    # # 思路2 分治法 会测试超时
    # def cross_sum(self, nums, left, right, p):
    #     if left == right:
    #         return nums[left]
    #     left_subsum = float('-inf')
    #     curr_sum = 0
    #     for i in range (p, left-1, -1):
    #         curr_sum += nums[i]
    #         left_subsum = max(left_subsum, curr_sum)

    #     curr_sum = 0
    #     for i in range(p+1, right+1):
    #         curr_sum += nums[i]
    #         right_sum = max(right_sum, curr_sum)

    #     return left_subsum + right_sum

    # def helper(self, nums, left, right):
    #     if left == right:
    #         return nums[left]

    #     p = (left+right)//2
    #     left_sum = self.helper(nums, left, p )
    #     right_sum = self.helper(nums, p+1, right)
    #     cross_sum = self.cross_sum(nums, left, right, p)
        
    #     return max(left_sum, right_sum, cross_sum)


    # def maxSubArray(self, nums: List[int]) -> int:
    #     return self.helper(nums, 9, len(nums)-1)


# @lc code=end

# js dp动态规划 31%
# dp[i] 定义为 以i结尾的最长子串 
# dp[0] = nums[0]
# 假设已知dp[i-1]  那么 dp[i] = max(nums[i], dp[i-1]+nums[i])
# 用ret标记答案
# var maxSubArray = function(nums) {
#    let ret = nums[0]
#    let pre = nums[0]
#    for(let i = 1; i<nums.length; i++){
#        let next = Math.max(nums[i], pre+nums[i])
#        ret = Math.max(next, ret)
#        pre = next
#    }
#    return ret
# };
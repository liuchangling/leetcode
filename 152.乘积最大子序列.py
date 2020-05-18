#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (37.40%)
# Likes:    515
# Dislikes: 0
# Total Accepted:    55.2K
# Total Submissions: 142.7K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
# dp思想，记录每一次乘以当前数之和的最大值和最小值，
# 并更新全局最大值ret




# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 测试用例没有[]
        # if len(nums) == 0:
        #     return 0

        nmin = nmax = ret = nums[0]

        for n in nums[1:]:
            nmin, nmax = min( n , n*nmax, n*nmin), max(n, n*nmax, n*nmin)
            ret = max(ret, nmax)
        return ret
# @lc code=end


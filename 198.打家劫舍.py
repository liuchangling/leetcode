#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (43.21%)
# Likes:    839
# Dislikes: 0
# Total Accepted:    126.2K
# Total Submissions: 278.4K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2:
# 
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 思路1 动态规划 96% 空间9%
# 扫了一眼dp吧 dp[i] = max (dp[i-2] + nums[i], dp[i-1])

# 思路2 对于思路1的空间优化
# 思路1 保存了整个dp数组，实际上只需要保存2个数即可

# 思路3 代码风格极简的思路2 98%

# @lc code=start
class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     # dp[i] = max (dp[i-2] + nums[i], dp[i-1])
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) <= 2:
    #         return max(nums)
    #     dp = []
    #     dp.append(nums[0])
    #     dp.append(max(nums[0], nums[1]))

    #     for i in range(2, len(nums)):
    #         dp.append(max(dp[i-2] + nums[i], dp[i-1] ))

    #     # print(dp)
    #     return dp[-1]

    # 不保存整个数组，
    # def rob(self, nums: List[int]) -> int:
    #     size = len(nums)
    #     if size == 0 : return 0
    #     if size == 1 : return nums[0]

    #     first = nums[0]
    #     second = max(nums[0], nums[1])

    #     for i in range(2, size):
    #         first, second = second, max(first + nums[i], second)
        
    #     return second

    def rob(self, nums: List[int]) -> int:
        cur , pre = 0 , 0
        for n in nums:
            cur , pre = max(pre+n, cur), cur

        return cur

# @lc code=end


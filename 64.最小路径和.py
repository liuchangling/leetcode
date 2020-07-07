#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (65.55%)
# Likes:    504
# Dislikes: 0
# Total Accepted:    97.7K
# Total Submissions: 148.1K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
# 简单dp 56 ms 82.28%
# 空间优化方向： 不需要用额外的 dp 数组，而是在原数组上存储，这样就不需要额外的存储空间。这里没有用
# 因为个人不太喜欢改变原始数据的值

# @lc code=start
class Solution:
    # 56 ms 82.28%
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0 :
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        

        return dp[-1][-1]
# @lc code=end


#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (60.41%)
# Likes:    550
# Dislikes: 0
# Total Accepted:    108.2K
# Total Submissions: 178.7K
# Testcase Example:  '3\n2'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
# 
# 
# 
# 示例 1:
# 
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 
# 
# 示例 2:
# 
# 输入: m = 7, n = 3
# 输出: 28
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10 ^ 9
# 
# 一看就是个入门级的dp。。。为什么没有先学这个玩意
# dp[i][j] = dp[i-1][j]+dp[i][j-1] 86%
# 看了一下答案，2分钟想到最优解，并写出bug free 代码，开心。一次过~

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for j in range(n)] for i in range(m)]
        

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        
        return dp[-1][-1]




# @lc code=end


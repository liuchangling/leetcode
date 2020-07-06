#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.46%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    72.4K
# Total Submissions: 208.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
#
# 入门dp题 36ms 94%
#
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 这一行会加12ms的运行时间。。。 去掉后击败94%。然而这一行是有用的。
        # if not obstacleGrid or not obstacleGrid[0]: return 0 

        m, n  = len(obstacleGrid), len(obstacleGrid[0])
        # dp[i][j] 定义为从左上角走到i,j坐标的可能路径数目
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1: return 0 # 左上角有block就直接返回0

        # dp[0][0]初始化为1
        dp[0][0] = 1 

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1 : 
                    dp[i][j] = 0 
                else :
                    if i > 0:
                        dp[i][j] += dp[i-1][j] 
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
                
        return dp[-1][-1]
# @lc code=end


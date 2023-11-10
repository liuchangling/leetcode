#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (63.78%)
# Likes:    489
# Dislikes: 0
# Total Accepted:    80.4K
# Total Submissions: 121.6K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 
# 
# 
# 例如，给定三角形：
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# 
# 思路1 dp 60ms 17%
# dp[i][j]表示到达该位置的最小路径和
# dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])

# 题目要求优化额外内存空间

# @lc code=start
class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     if not triangle : return 0 

    #     m = len(triangle)
    #     n = len(triangle[-1])

    #     dp = [[0 for i in range(n)] for _ in range(m)]

    #     dp[0][0] = triangle[0][0]
    #     for i in range(1,m):
    #         for j in range(0,i+1):
    #             if j == 0 :
    #                 dp[i][j] = triangle[i][j] + dp[i-1][j]
    #             elif j == i :
    #                 dp[i][j] = triangle[i][j] + dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
        
    #     return min(dp[-1])

    # 内存优化后的dp 48ms 71%
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle : return 0 

        m = len(triangle)

        dp = [0]*m
        dp[0] = triangle[0][0]

        for i in range(1,m):
            tmp = [0]*m
            for j in range(0,i+1):
                if j == 0 :
                    tmp[j] = triangle[i][j] + dp[j]
                elif j == i :
                    tmp[j] = triangle[i][j] + dp[j-1]
                else:
                    tmp[j] = triangle[i][j] + min(dp[j], dp[j-1])
            dp = tmp
        
        return min(dp)
# @lc code=end

# /**
#  * @param {number[][]} triangle
#  * @return {number}
#  */

# // dp[i][j] 定义为 到这个未知的最小路径和
# // 如果j = 0无需考虑j-1
# // dp[i][j] = arr[i][j] + min(dp[i-1][j-1], dp[i-1][j])
# // var minimumTotal = function (triangle) {

# //     const len = triangle.length
# //     dp = new Array(len)
# //     dp[0] = new Array()
# //     dp[0][0] = triangle[0][0]

# //     for (let i = 1; i < len; i++) {
# //         dp[i] = new Array()
# //         dp[i][0] = triangle[i][0] + dp[i - 1][0]
# //         for (let j = 1; j < i; j++) {
# //             dp[i][j] = triangle[i][j] + Math.min(dp[i - 1][j - 1], dp[i - 1][j])
# //         }
# //         dp[i][i] = triangle[i][i] + dp[i-1][i-1]

# //         // for (let j = 0; j <= i; j++) {
# //         //     dp[i][j] = triangle[i][j] + Math.min(j > 0 ? dp[i - 1][j - 1] : Infinity, j < i ? dp[i - 1][j] : Infinity)
# //         // }
# //     }

# //     return Math.min(...dp[len - 1])
# // };



# // var minimumTotal = function (triangle) {

# //     const len = triangle.length
# //     // 空间压缩
# //     pre = new Array(len)
# //     cur = new Array(len)
# //     pre[0] = triangle[0][0]

# //     for (let i = 1; i < len; i++) {
# //         for (let j = 0; j <= i; j++) {
# //             cur[j] = triangle[i][j] + Math.min(j > 0 ? pre[j - 1] : Infinity, j < i ? pre[j] : Infinity)
# //         }
# //         pre = cur.slice()
# //     }

# //     return Math.min(...pre)
# // };
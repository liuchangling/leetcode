#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (38.83%)
# Likes:    382
# Dislikes: 0
# Total Accepted:    61.1K
# Total Submissions: 152.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#
# 示例 2:
#
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# 我的思路很简单，就是模拟坐标走一遍。有些边界要稍微考虑一下。 83%
# 和官方题解2比较类似。 另外官方题解1提供了辅助一个visited矩阵来做，代码会好看点，但是额外空间较大

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        if bottom < 0 : return matrix

        left, right = 0, len(matrix[0]) - 1

        curX, curY, direction = 0, 0, 0
        ans = []

        while left <= right and top <= bottom:
            if direction == 0:  # to right
                ans += matrix[curX][left:right+1]
                curX = bottom
                curY = right
                top += 1
            elif direction == 1:  # to bottom
                for d in matrix[top:bottom+1]:
                    ans.append(d[curY])
                curX = bottom
                curY = left
                right -= 1
            elif direction == 2:  # to left
                end = left - 1 if left > 0 else None
                ans += matrix[curX][right: end: -1]
                curX = top
                curY = left
                bottom -= 1
            else:  # to top
                for d in matrix[bottom:top-1:-1]:
                    ans.append(d[curY])
                curX = top
                curY = right
                left += 1

            direction = (direction + 1) % 4

        return ans
# @lc code=end

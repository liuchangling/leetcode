#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (76.71%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    35.7K
# Total Submissions: 46K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
# 一次过系列 用的是54题的思路1。 如果下一个要访问的坐标越界或者已经处理过，就改变方向。

# 思路2 上下左右边界处理 95% 我写的没有range(xxx).速度快很多。

# @lc code=start
class Solution:
    # 思路1  15%
    # def generateMatrix(self, n: int) -> List[List[int]]:
    # direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # ans = [[0 for i in range(n)] for j in range(n)]
    # row, col, d = 0, 0, 0
    # i, final = 1, n*n

    # while i <= final:
    #     ans[row][col] = i

    #     nr = row + direction[d][0]
    #     nc = col + direction[d][1]

    #     if nr >= n or nr < 0 or nc >= n or nc < 0 or ans[nr][nc] > 0:
    #         d = (d+1) % 4

    #     row += direction[d][0]
    #     col += direction[d][1]
    #     i += 1

    # return ans

    # 思路2  上下左右边界处理 95%
    def generateMatrix(self, n: int) -> List[List[int]]:

        ans = [[0 for i in range(n)] for j in range(n)]

        left, top, right, bottom = 0, 0, n-1, n-1
        x, y = 0, 0
        i, final = 1, n*n

        while i < final:  # 这里如果写了=会死循环，因为奇数情况不会触发到中间那个点
            while y < right:
                ans[x][y] = i
                y += 1
                i += 1

            top += 1

            while x < bottom:
                ans[x][y] = i
                x += 1
                i += 1

            right -= 1

            while y > left:
                ans[x][y] = i
                y -= 1
                i += 1

            bottom -= 1

            while x > top:
                ans[x][y] = i
                x -= 1
                i += 1

            left += 1

        ans[x][y] = i

        return ans

    # 思路2 简洁版本 67%
    # def generateMatrix(self, n: int) -> List[List[int]]:
    #     left, right , top, bottom = 0, n-1, 0, n-1
    #     matrix = [[0] * n for _ in range(n)]
    #     num, target = 1, n **2

    #     while num <= target:
    #         for i in range(left, right+1):
    #             matrix[top][i] = num
    #             num += 1
    #         top += 1

    #         for i in range(top,bottom+1):
    #             matrix[i][right]= num
    #             num += 1
    #         right -= 1

    #         for i in range(right,left-1,-1):
    #             matrix[bottom][i] = num
    #             num += 1
    #         bottom -= 1

    #         for i in range(bottom, top-1, -1):
    #             matrix[i][left] = num
    #             num += 1
    #         left += 1
    #     return matrix

# @lc code=end

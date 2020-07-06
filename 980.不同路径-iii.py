#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#
# https://leetcode-cn.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (70.26%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 8.9K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# 在二维网格 grid 上，有 4 种类型的方格：
#
#
# 1 表示起始方格。且只有一个起始方格。
# 2 表示结束方格，且只有一个结束方格。
# 0 表示我们可以走过的空方格。
# -1 表示我们无法跨越的障碍。
#
#
# 返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。
#
#
#
# 示例 1：
#
# 输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# 输出：2
# 解释：我们有以下两条路径：
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
# 示例 2：
#
# 输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# 输出：4
# 解释：我们有以下四条路径：
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
# 示例 3：
#
# 输入：[[0,1],[2,0]]
# 输出：0
# 解释：
# 没有一条路能完全穿过每一个空的方格一次。
# 请注意，起始和结束方格可以位于网格中的任意位置。
#
#
#
#
# 提示：
#
#
# 1 <= grid.length * grid[0].length <= 20
#
#
# 思路1 dfs回溯  68ms 73%
# 注意回溯的backtrack是不能加lruCache的，因为这个涉及grid变更
# 准备工作：统计路径长度，起点位置
# 回溯过程：
#   不能走的， 直接return0
#   能走的，把gird[i][j]标记为-1，然后向着四个方向dfs遍历
#
# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        step = 0  # 统计总共路线长度
        for col in range(m):
            for row in range(n):
                if grid[col][row] == -1:
                    pass
                elif grid[col][row] == 1:
                    startX, startY = col, row
                else:  # 0 or 2
                    step += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        
        def backtrack(i: int, j: int, level: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0  # 剪枝1：数组越界

            if grid[i][j] == -1:
                return 0  # 剪枝2：又踩到了踩过的

            if grid[i][j] == 2:  # 剪枝3：提前踩终点
                return 1 if level == 0 else 0

            grid[i][j] = -1 # 做选择，即踩下
            count = 0  # 统计可能性
            for x, y in directions:
                count += backtrack(i+x, j+y, level-1) #遍历 这里其实是dfs的步骤
            grid[i][j] = 0 # 回溯选择，即还原为0

            return count

        return backtrack(startX, startY, step)  # start


# @lc code=end

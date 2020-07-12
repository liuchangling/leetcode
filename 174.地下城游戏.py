#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#
# https://leetcode-cn.com/problems/dungeon-game/description/
#
# algorithms
# Hard (41.20%)
# Likes:    276
# Dislikes: 0
# Total Accepted:    17K
# Total Submissions: 37.4K
# Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
#
# 
# table.dungeon, .dungeon th, .dungeon td {
# ⁠ border:3px solid black;
# }
# 
# ⁠.dungeon th, .dungeon td {
# ⁠   text-align: center;
# ⁠   height: 70px;
# ⁠   width: 70px;
# }
# 
# 
# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N
# 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为
# 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 
# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。
# 
# 
# 
# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
# 
# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
# 
# 
# ⁠
# -2 (K) 
# -3 
# 3 
# ⁠
# ⁠
# -5 
# -10 
# 1 
# ⁠
# ⁠
# 10 
# 30 
# -5 (P) 
# ⁠
# 
# 
# 
# 
# 
# 说明:
# 
# 
# 
# 骑士的健康点数没有上限。
# 
# 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
# 
# dp[i][j][0] 代表到达这个格子所需最少初始hp。和剩余hp
# dp[i][j][0] 代表按最少初始hp开始的情况下，当前剩余hp
# dp[0][0] = (max(-dungeon[0][0] ,0 ), max(dungeon[0][0], 0 ))
# 
# 我们要保证的是dp[i][j][1] >= 0 的前提下， dp[i][j][0]最小
# 但是这个解法是错的，原因 有时候 最低0 剩余1 最低2 剩余4
# 然后如果之前把2-4的答案丢了，那么答案就是错的。


# 官方题解，逆序搞，那么久没有剩余hp的考虑了
# 我们从右下角走到左上角
# dp[i][j] 表示从坐标 (i,j) 到终点所需的最小初始值。
# 显然dp[m-1][n-1] = max(1, -dungeon[m-1][n-1])
# dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon: return 0
        m,n = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for m in range(n + 1) ] for _ in range(m + 1)]
        
        dp[m-1][n] = dp[m][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        
        return dp[0][0]


    # failed at  [[1,-3,3],[0,-2,0],[-3,-3,-3]]
    # def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    #     if not dungeon : return 0

    #     m,n = len(dungeon), len(dungeon[0])

    #     dp = [[[0,0] for m in range(n) ] for _ in range(m)]

    #     dp[0][0] = [max(-dungeon[0][0] ,0 ), max(dungeon[0][0], 0 )]

    #     for i in range(1,m):
    #         add_a = 0 if dp[i-1][0][1] + dungeon[i][0] >= 0 else -dungeon[i][0] - dp[i-1][0][1]
    #         dp[i][0][0] = add_a + dp[i-1][0][0]
    #         dp[i][0][1] = dp[i-1][0][1] + dungeon[i][0] + add_a
        
    #     for j in range(1,n):      
    #         add_b = 0 if dp[0][j-1][1] + dungeon[0][j] >= 0 else -dungeon[0][j] - dp[0][j-1][1]
    #         dp[0][j][0] = add_b + dp[0][j-1][0]
    #         dp[0][j][1] = dp[0][j-1][1] + dungeon[0][j] + add_b



    
    #     for i in range(1,m):
    #         for j in range(1,n):
    #             # 我们要保证的是dp[i][j][1] >= 0 的前提下， dp[i][j][0]最小
    #             cur = dungeon[i][j]
    #             add_a = 0 if dp[i-1][j][1] + cur >= 0 else -cur - dp[i-1][j][1]
    #             add_b = 0 if dp[i][j-1][1] + cur >= 0 else -cur - dp[i][j-1][1]


    #             # print(add_a, add_b,  add_a + dp[i-1][j][0] , add_b + dp[i][j-1][0])
    #             if add_a + dp[i-1][j][0] < add_b + dp[i][j-1][0]:
    #                 dp[i][j][0] = add_a + dp[i-1][j][0]
    #                 dp[i][j][1] = dp[i-1][j][1] + cur + add_a
    #             else:
    #                 dp[i][j][0] = add_b + dp[i][j-1][0]
    #                 dp[i][j][1] = dp[i][j-1][1] + cur + add_b
                    
    #     print(dp)

    #     return dp[-1][-1][0] + 1 # 因为等于0会死，所以加1
# @lc code=end


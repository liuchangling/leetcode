# 在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。

# 我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区  [{1}, {2,2}, {3,3}, {2}, {1,1}]。）

# 给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：

# houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
# cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
# 请你返回最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区，如果没有涂色方案，请返回 -1 。

 

# 示例 1：

# 输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# 输出：9
# 解释：房子涂色方案为 [1,2,2,1,1]
# 此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
# 涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
# 示例 2：

# 输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# 输出：11
# 解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
# 此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
# 给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
# 示例 3：

# 输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
# 输出：5
# 示例 4：

# 输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
# 输出：-1
# 解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。
 

# 提示：

# m == houses.length == cost.length
# n == cost[i].length
# 1 <= m <= 100
# 1 <= n <= 20
# 1 <= target <= m
# 0 <= houses[i] <= n
# 1 <= cost[i][j] <= 10^4


# 房子  颜色  街道数 = 总花费
# dp[i][j][k] = min(dp[i-1][j][k] ,dp[i-1][各种非j][k-1]) + cost[i][j]

# 哈哈哈哈 第一次没看答案作对的竞赛hard，  虽然离比赛已经过去了40分钟。。。
# 这个玩意，去掉dp之后要稍微处理一下house[i]数组，cost记成0

from typing import List
import sys

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        dp = [[[sys.maxsize for k in range(target + 1)] for j in range(n)] for i in range(m)]

        if houses[0] > 0:
            dp[0][houses[0]-1][1] = 0
        else :
            for j in range(n):            
                dp[0][j][1] = cost[0][j] 
        
        for i in range(1, m):
            for j in range(n):
                for k in range(1,target+1):

                    if houses[i] > 0 : # 颜色不可达
                        if houses[i] - 1 != j:
                            dp[i][j][k] = sys.maxsize  # 直接赋为maxsize 继续下一次循环
                            continue
                        else :
                            cost[i][j] = 0  #否则将cost设置为0继续常规计算
                    
                   
                    m = dp[i-1][j][k] # 上一次也是颜色j时，街道数不变，即k不变
                    
                    # 对于k大于1的情况，可能出现街道增加的情况，在所有颜色中找到最小值
                    if k > 1:
                        for x in range(n):# 上一次颜色不同,街道数增加
                            if x != j:
                                m = min(m, dp[i-1][x][k-1])

                    dp[i][j][k] = m + cost[i][j]

        ans = sys.maxsize
        for j in range(n):
            ans = min(ans, dp[-1][j][target])

        if ans == sys.maxsize: ans = -1

        return ans



Solution().minCost([0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3)
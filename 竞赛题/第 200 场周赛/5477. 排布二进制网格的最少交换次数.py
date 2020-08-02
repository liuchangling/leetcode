# 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。

# 一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。

# 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。

# 主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。

 

# 示例 1：



# 输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
# 输出：3
# 示例 2：



# 输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# 输出：-1
# 解释：所有行都是一样的，交换相邻行无法使网格符合要求。
# 示例 3：



# 输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
# 输出：0
 

# 提示：

# n == grid.length
# n == grid[i].length
# 1 <= n <= 200
# grid[i][j] 要么是 0 要么是 1 。

# 题目要的是右上角全0
# 统计目前每一行右侧连续0的个数  Map<i:int,count:int>
# 贪心算法，第一步我们先将满足count大于等于 n-1的行中最小的一个移动到最上面
# 所以我们要做的是，每次在符合要求的count中，选取行号最小的，交换到最上面。统计步数并输出
# 如果找不到符合要求的count就返回-1

class Solution:    
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        m = []

        for i in range(n):
            count = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    m.append(count)
                    break
                else:
                    count += 1
                    if j == 0:
                        m.append(count)

        ans = 0 
        
        for i in range(n):
            need = n - i - 1
            found = -1

            for j in range (n):
                if m[j] >= need:
                    found = j
                    # m[i:j] -> m[i+1:j]  然后m[j]插入m[i]的位置
                    m.pop(j)
                    m.insert(i,-1)
                    break
            if found >= 0:
                ans += (found - i)
            else :
                return -1
        
        return ans
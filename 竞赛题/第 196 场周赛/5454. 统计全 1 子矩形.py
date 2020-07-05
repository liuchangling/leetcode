# 5454. 统计全 1 子矩形
# 给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

 

# 示例 1：

# 输入：mat = [[1,0,1],
#             [1,1,0],
#             [1,1,0]]
# 输出：13
# 解释：
# 有 6 个 1x1 的矩形。
# 有 2 个 1x2 的矩形。
# 有 3 个 2x1 的矩形。
# 有 1 个 2x2 的矩形。
# 有 1 个 3x1 的矩形。
# 矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
# 示例 2：

# 输入：mat = [[0,1,1,0],
#             [0,1,1,1],
#             [1,1,1,0]]
# 输出：24
# 解释：
# 有 8 个 1x1 的子矩形。
# 有 5 个 1x2 的子矩形。
# 有 2 个 1x3 的子矩形。
# 有 4 个 2x1 的子矩形。
# 有 2 个 2x2 的子矩形。
# 有 2 个 3x1 的子矩形。
# 有 1 个 3x2 的子矩形。
# 矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
# 示例 3：

# 输入：mat = [[1,1,1,1,1,1]]
# 输出：21
# 示例 4：

# 输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
# 输出：5
 

# 提示：

# 1 <= rows <= 150
# 1 <= columns <= 150
# 0 <= mat[i][j] <= 1


# 思路1  当时想法是，每次把以当前结尾的都找出来，然后sum

#  优化思路  dp为左边（或者上面）连续1的个数。 然后计算sum，有一定优化
#  实现是copy的

from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        m = len(mat) 
        n = len(mat[0])

        dp = [[0 for _ in range(n)] for i in range(m)]

        dp[0][0] =  mat[0][0]


        for i in range(m):
            for j in range(n):


                
                if mat[i][j] == 1 :
                    tmp = 0                    
                    x = i
                    xmin = -1
                    while x >= 0 :
                        y = j
                        if mat[x][y] == 0: 
                            x = -1
                        else:
                            while y >= 0 and y>xmin:
                                if mat[x][y]:
                                    tmp += 1
                                    y -= 1
                                else:
                                    xmin = max(xmin, y)
                                    break

                            x -= 1
                
                    
                    dp[i][j] = tmp

        # print(dp)
        return sum([sum(_) for _ in dp])
        

    # 优化思路 

    # def numSubmat(self, mat: List[List[int]]) -> int:
    #         rows, cols = len(mat), len(mat[0])
    #         dp = []
    #         for i in range(rows + 1):
    #             dp.append([0] * (cols + 1))
    #         ans = 0
    #         for i in range(rows - 1, -1, -1):
    #             for j in range(cols - 1, -1, -1):
    #                 if mat[i][j] == 0:
    #                     continue
    #                 dp[i][j] = dp[i][j + 1] + 1
    #                 minVal = 150
    #                 for x in range(i, rows):
    #                     minVal = min(minVal, dp[x][j])
    #                     ans += minVal
    #                     if minVal == 0:
    #                         break
    #         return ans
print(Solution().numSubmat([[1,1,1,1,0],[1,0,0,1,0],[0,0,1,0,1],[0,1,0,0,0]]))#17
                        



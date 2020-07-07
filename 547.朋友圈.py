#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (55.08%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    50.5K
# Total Submissions: 88.1K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
# 
# 示例 1:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
# 
# 
# 注意：
# 
# 
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
# 思路1 并查集
# 秒写的并查集，感觉这个数据虽然少见，但是实现很简单。
# 核心就是rootList[getRoot(i)] = getRoot(j) 这个union操作记号之后，后面就没啥难度了
# 最坏为o(n^3)
# 并查集 288ms 31%
#
# 思路2 dfs 时间复杂度为O(n2)
# 学习一下邻接矩阵的dfs， bfs同理
# for i in range(n): if not visited[i]: dfs(i)
# 递归 228ms 84%
# 276 ms 36% 迭代

# 思路3 bfs 时间复杂度O(n2) 264ms 61%


# @lc code=start

class Solution:
    # 思路1 并查集 288ms 31%
    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     n = len(M)
    #     rootList = list(range(n))

    #     # query
    #     def getRoot(i): 
    #         while rootList[i] != i:
    #             i = rootList[i]
    #         return i

    #     # union
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             if M[i][j] == 1:
    #                 rootList[getRoot(i)] = getRoot(j)


    #     # use query get ans
    #     ans = set()    	
    #     for i in range(n):
    #         ans.add(getRoot(i))


    #     return len(ans)

    # # 思路2  dfs 276 ms 36% 迭代
    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     n = len(M)
    #     ans = 0 

    #     def dfs(i):
    #         stack = [i]

    #         while stack:
    #             node = stack.pop()

    #             for j in range(n):
    #                 if M[node][j] == 1 and visited[j] == False:
    #                     visited[j] = True
    #                     stack.append(j)

    #     visited = [False for _ in range(n)]
    #     for i in range(n):
    #         if not visited[i]:
    #             dfs(i)
    #             ans +=1

    #     return ans 

    # 思路2 递归 228ms 84%
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        ans = 0 

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if M[i][j] == 1 and not visited[j]:
                    dfs(j)

        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans +=1

        return ans 


    # 思路3 bfs 264ms 61%
    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     n = len(M)
    #     ans = 0 

    #     def bfs(i):
    #         queue = [i]
    #         while queue:
    #             node = queue.pop(0)
    #             visited[node] = True
    #             for j in range(n):
    #                 if not visited[j] and M[node][j] == 1:
    #                     queue.append(j)


    #     visited = [False for _ in range(n)]
    #     for i in range(n):
    #         if not visited[i]:
    #             bfs(i)
    #             ans +=1

    #     return ans 
        
# @lc code=end


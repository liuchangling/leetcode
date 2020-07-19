# 给你一棵树（即，一个连通的无环无向图），这棵树由编号从 0  到 n - 1 的 n 个节点组成，且恰好有 n - 1 条 edges 。树的根节点为节点 0 ，树上的每一个节点都有一个标签，也就是字符串 labels 中的一个小写字符（编号为 i 的 节点的标签就是 labels[i] ）

# 边数组 edges 以 edges[i] = [ai, bi] 的形式给出，该格式表示节点 ai 和 bi 之间存在一条边。

# 返回一个大小为 n 的数组，其中 ans[i] 表示第 i 个节点的子树中与节点 i 标签相同的节点数。

# 树 T 中的子树是由 T 中的某个节点及其所有后代节点组成的树。

from collections import defaultdict
from functools import lru_cache
from collections import Counter

# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#         visited = [False] * n

#         counterMap = [defaultdict(int) for _ in range(n)]

#         @lru_cache(None)
#         def dfs(node: int) -> int:
#             visited[node] = True

#             counter = defaultdict(int)
#             counter[labels[node]] = 1

#             for i,j in edges:
#                 if not visited[j] and i == node:
#                     tmp = dfs(j)
#                     for key in tmp:
#                         counter[key] += tmp[key]


#                 elif not visited[i] and j == node:
#                     tmp = dfs(i)
#                     for key in tmp:
#                         counter[key] += tmp[key]

#             counterMap[node] = counter
            
#             return counter



#         dfs(0)

#         # print (counterMap)
        
#         ans = [0] * n
        
#         for i in range(n):
#             ans[i] = counterMap[i][labels[i]]



#         return ans





# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#         edgesMap = defaultdict(list)

#         for i,j in edges:
#             edgesMap[i] += [j]
#             edgesMap[j] += [i]

#         visited = [False] * n

#         counterMap = [defaultdict(int) for _ in range(n)]

#         @lru_cache(None)
#         def dfs(node: int) -> int:
#             visited[node] = True

#             counter = defaultdict(int)
#             counter[labels[node]] = 1

#             for nextNode in edgesMap[node]:
#                 if not visited[nextNode]:
#                     tmp = dfs(nextNode)
#                     for key in tmp:
#                         counter[key] += tmp[key]


#             counterMap[node] = counter            
#             return counter


#         dfs(0)
        
#         ans = [0] * n
        
#         for i in range(n):
#             ans[i] = counterMap[i][labels[i]]
            

#         return ans


# dfs 会递归超过上限
# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#         edgesMap = defaultdict(list)

#         for i,j in edges:
#             edgesMap[i] += [j]
#             edgesMap[j] += [i]


#         counter = [[0] * 26 for _ in range(n)]
#         visited = [False] * n

#         @lru_cache(None)
#         def dfs(node: int) -> int:
#             n = ord(labels[node]) - ord('a')
#             counter[node][n] = 1
#             visited[node] = True

#             for nextNode in edgesMap[node]:
#                 if not visited[nextNode]:
#                     dfs(nextNode)
#                     for ch in range(26):
#                         counter[node][ch] += counter[nextNode][ch]
#         dfs(0)
#         ans = [0] * n
        
#         for i in range(n):
#             ans[i] = counter[i][ord(labels[i]) - ord('a')]
        
#         return ans


# dfs 2604 ms 100.00%
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        edgesMap = defaultdict(list)

        for i,j in edges:
            edgesMap[i] += [j]
            edgesMap[j] += [i]

        def dfs(i):
            visited.add(i)
            # 字符数字典
            data = Counter({labels[i]: 1})
            for nxt in edgesMap[i]:
                if nxt not in visited: 
                    # 整合子树的字符数
                    data += dfs(nxt)
            # 设置当前节点的结果字符数
            ans[i] = data[labels[i]]
            return data

        visited = set()
        ans = [1] * n
        dfs(0)
        return ans
        


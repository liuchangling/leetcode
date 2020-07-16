#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
# https://leetcode-cn.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (43.41%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    10.5K
# Total Submissions: 22.3K
# Testcase Example:  '[[1,3],[0,2],[1,3],[0,2]]'
#
# 给定一个无向图graph，当这个图为二分图时返回true。
# 
# 如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
# 
# 
# graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边：
# graph[i] 中不存在i，并且graph[i]中没有重复的值。
# 
# 
# 
# 示例 1:
# 输入: [[1,3], [0,2], [1,3], [0,2]]
# 输出: true
# 解释: 
# 无向图如下:
# 0----1
# |    |
# |    |
# 3----2
# 我们可以将节点分成两组: {0, 2} 和 {1, 3}。
# 
# 
# 
# 
# 示例 2:
# 输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
# 输出: false
# 解释: 
# 无向图如下:
# 0----1
# | \  |
# |  \ |
# 3----2
# 我们不能将节点分割成两个独立的子集。
# 
# 
# 注意:
# 
# 
# graph 的长度范围为 [1, 100]。
# graph[i] 中的元素的范围为 [0, graph.length - 1]。
# graph[i] 不会包含 i 或者有重复的值。
# 图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
# 
# 
# 思路1 bfs 448ms 5%
# 访问数组visited -1表示未访问， 0表示放在左边， 1表示放在右边
# 对所有节点遍历，如果未访问过，对可达节点继续遍历，这是一个bfs的过程
# 一次过，但性能较差

# 思路2 bfs 220ms 62%
# 1.优化了queue内的存储，直接使用visited的数字标识已染色的点
# 2.将visited优化为map，提高查找速度
# 3.使用异或^替代了- 加快运行速度

# 思路3 dfs
# 递归需要用nonlocal关键字
# 非递归代码好看点

# @lc code=start
class Solution:
    # def isBipartite(self, graph: List[List[int]]) -> bool:

    #     if not graph: return False
        
    #     n = len(graph)
    #     # -1 not visited 0 left 1 right
    #     visited = [-1 for _ in range(n)]

    #     for i in range(n):
    #         if visited[i] == -1:
    #             queue = [(i, 0)]

    #             while queue:
    #                 idx, direction = queue.pop(0)
    #                 visited[idx] = direction
                    
    #                 for j in graph[idx]:
    #                     if visited[j] == -1:                            
    #                         queue.append((j, 1 - direction))
    #                     elif visited[j] != 1 - direction:
    #                         return False

    #     # print(visited)
    #     return True

    # 思路2 BFS优化内存空间  220ms 67%
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # if not graph: return False
        
        n = len(graph)
        # not i= not visited 0 left 1 right
        visited = {}

        for i in range(n):
            if i not in visited:
                queue = [i]
                visited[i] = 0 

                while queue:
                    idx = queue.pop(0)
                    direction = visited[idx] 
                    
                    for j in graph[idx]:
                        if j not in visited:
                            visited[j] = 1 ^ direction
                            queue.append(j)
                        elif visited[j] != 1 ^ direction:
                            return False

        # print(visited)
        return True
    
    # 思路3 DFS优化内存空间  220ms 67% 时间差不多
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0 
                stack = [i]

                while stack:
                    idx = stack.pop()
                    direction = color[idx]
                    
                    for j in graph[idx]:
                        if j not in color:
                            color[j] = 1^direction
                            stack.append(j)
                        elif color[j] != 1^direction:
                            return False       
       
        return True
        
# @lc code=end


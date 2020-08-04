#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (51.16%)
# Likes:    497
# Dislikes: 0
# Total Accepted:    63.8K
# Total Submissions: 119.3K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
# 
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
# 
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
# 
# 
# 
# 示例 1:
# 
# 输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 
# 示例 2:
# 
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
# 
# 
# 
# 提示：
# 
# 
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
# 
# 
# 好像是有向图判环问题？ 实际上是一个经典拓扑排序题
# 思路1 BFS  44ms 96%
# 计算入度， 直接得出路径。 
# queue初始化为入度为0 的节点
# 取出节点后，更新入度数组，如果有节点入度变为0，则插入queue
# 这个BFS的遍历和插入比较有趣，仔细看看


# 思路2 DFS
# 计算出度，得出路径的逆序，稍微有点绕
# 这里我们对每个节点有三种状态 0-未搜索  1-搜索中  2-已搜索
# 可以从任意节点开始搜索，同时更新出度 
# 遍历过程中如果遇到搜索中的节点（1） 就代表有环
# 这个过程更像直觉中走路看有没有环的问题。 代码稍微难一点

from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    # 思路1 bfs 44ms 96%
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     indeg = [0] * numCourses # 每个节点的入度
    #     m = defaultdict(list) # 用于计算每个节点的下一个节点，方便进行入度-1操作
    #     # 预处理
    #     for cur,before in prerequisites:
    #         m[before].append(cur)
    #         indeg[cur] += 1
        
    #     # 开始把入度为0的插入queue  如果每个节点入度都大于0 ，则有环，无法完成拓扑排序。
    #     queue = [_ for _ in range(numCourses) if indeg[_] == 0]

    #     visited = 0 

    #     while queue:            
    #         node = queue.pop(0)
    #         visited += 1
    #         for idx in m[node]:
    #             indeg[idx] -= 1
    #             if indeg[idx] == 0:
    #                 queue.append(idx)

        
    #     return visited == numCourses

    # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        status = [0] * numCourses # 状态
        m = defaultdict(list) # 提前找好下一个节点有哪些
        for cur,before in prerequisites:
            m[before].append(cur)

        invalid = False # 因为遇到环可以直接return 所以设置了invalid变量
        visited = 0  # 用于记录已访问的节点个数， 这个玩意和bfs一样

        def dfs(i):
            nonlocal invalid  
            nonlocal visited
            
            status[i] = 1  # 标记为搜索中

            for child in m[i]:
                if status[child] == 0: # dfs遍历status = 0 
                    dfs(child)
                    if invalid: 
                        return
                elif status[child] == 1: # return when status = 1                
                    invalid = True
                    return
                # ignore status = 2
            
            status[i] = 2 # 后续节点都访问玩了，标记为已搜索
            visited += 1 # 又完成了一个节点

        for i in range(numCourses):
            if not invalid and status[i] == 0: # 注意这里也加了invalid控制，可以提前退出
                dfs(i)

        return visited == numCourses

        



# @lc code=end
Solution().canFinish(2, [[1,0]])
# Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：

# 类型 1：只能由 Alice 遍历。
# 类型 2：只能由 Bob 遍历。
# 类型 3：Alice 和 Bob 都可以遍历。
# 给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

# 返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

 

# 示例 1：



# 输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# 输出：2
# 解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。
# 示例 2：



# 输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# 输出：0
# 解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。
# 示例 3：



# 输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# 输出：-1
# 解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。
 

# 提示：

# 1 <= n <= 10^5
# 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
# edges[i].length == 3
# 1 <= edges[i][0] <= 3
# 1 <= edges[i][1] < edges[i][2] <= n
# 所有元组 (typei, ui, vi) 互不相同

# 显然优先使用type3
# 如果Alice和Bob的路径为可连通图，那么

# 方法1 dfs 
# 1) 写一个方法用于计算每种路径可以组成几个可连通图
# 2) 如果type1 或者 type2 的可连通图大于1 说明为非连通 返回-1
# 3) 如果type3 的可连通图数 = 1，说明type3中选取n-1条边即可满足条件，所以返回len(edges) - (n-1)
# 4）如果type3 的可连通图数 = x, 仔细理解一下，type3中，选用的边是 n-x条
#    对于Alice和Bob来说，都需要做一件事，就是将这x个连通图，变成一个连通图，显然每个人都要增加 2(x-1)条边
#    所以必须的边数为: n-x + 2(x-1) = n+x -2
#    所以 return len(edges) - (n+x-2)



# 方法2 并查集
# 1.先把type3 带上 尽可能多的添加可访问节点。 能构成一起的组成并查集
# 2.对于type1 遍历并增加对应边
# 3.对于type2 做类似2的操作
# 剩余的边数就是不要的



from typing import List
from collections import defaultdict
class Solution:
    # dfs 1092 ms 
    # def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    #     AlicePath = defaultdict(set)
    #     BobPath = defaultdict(set)
    #     CommonPath = defaultdict(set)
    #     for type, u, v in edges:
    #         if type == 1 or type == 3 :
    #             AlicePath[u-1].add(v-1)
    #             AlicePath[v-1].add(u-1)
    #         if type == 2 or type == 3 :
    #             BobPath[u-1].add(v-1)
    #             BobPath[v-1].add(u-1)
    #         if type == 3:
    #             CommonPath[u-1].add(v-1)
    #             CommonPath[v-1].add(u-1)

    #     # 计算一组边可以拆分为几组可连通图
    #     def count(m: defaultdict(set)):
    #         visited = [False] * n
    #         ret = 0 
            
    #         def dfs(i: int, isNewGraph:bool):
    #             nonlocal ret
    #             if visited[i]: return 
    #             visited[i] = True
    #             # 外层遍历时，为新图。内部递归时为旧的连通图，无需增加统计数目
    #             if isNewGraph: ret += 1 
    #             for endPoint in m[i]:
    #                 dfs(endPoint, False)

    #         for i in range(n):
    #             dfs(i, True) # 这里True表示是从外层开始dfs，遇到没有访问过的节点就需要将计数+1

    #         return ret

    #     if count(AlicePath) > 1 or count(BobPath)> 1 :
    #         return -1

    #     x = count(CommonPath)
    #     return len(edges) - (n+x-2)

    # union set # 很遗憾这个写法会TLE
    # def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    #     AliceUnion = list(range(n))
    #     BobUnion = list(range(n))
    #     CommonUnion = list(range(n))

    #     # query
    #     def getRoot(i:int, unionset:List[int]):
    #         while unionset[i] != i:
    #             i = unionset[i]
    #         return i

    #     # union       
    #     for type, u, v in edges:
    #         if type == 1 or type == 3 :
    #             AliceUnion[getRoot(u-1, AliceUnion)] = getRoot(v-1, AliceUnion)
    #         if type == 2 or type == 3 :
    #             BobUnion[getRoot(u-1, BobUnion)] = getRoot(v-1, BobUnion)
    #         if type == 3:
    #             CommonUnion[getRoot(u-1, CommonUnion)] = getRoot(v-1, CommonUnion)
       
    #     # 计算一组边可以拆分为几组可连通图
    #     def count(unionset: List[int]):
    #         visited = set()
    #         ret = 0 
    #         for i in range(n):
    #             root = getRoot(i, unionset)
    #             if root not in visited:
    #                 ret += 1
    #                 visited.add(root)
    #         return ret

    #     if count(AliceUnion) > 1 or count(BobUnion)> 1 :
    #         return -1

    #     x = count(CommonUnion)
    #     return len(edges) - (n+x-2)


    # union set #344 ms
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        AliceUnion = list(range(n))

        # query
        def getRoot(i:int, unionset:List[int]):
            while unionset[i] != i:
                i = unionset[i]
            return i

        # union
        def union(u:int, v:int, unionset:List[int]):
            s = getRoot(u-1, unionset)
            e = getRoot(v-1, unionset)
            if s == e :
                return False
            else:
                # 通常只要写 unionset[s] = e即可
                # 这里把root统一指向最大值，加速后续查找getRoot效率
                m = max(s,e,u-1,v-1)
                unionset[s] = m
                unionset[e] = m
                unionset[u-1] = m
                unionset[v-1] = m
                return True # 表示添加一条有效边

        a = 0 # 记录已添加的有效边数
        # 先统计common的
        for type, u, v in edges:
            if type == 3:
                if union(u, v, AliceUnion) : a += 1
        
        #然后把alice的 copy给Bob
        BobUnion = AliceUnion.copy()
        b = a 
        x = n - a # 记录公共路径连通数 保持和思路1一致的写法。也可以不用这个

        # 公共路径是一个完整连通图直接返回
        if x == 1 : return len(edges) - (n-1)

        # 否则判断Alice 和Bob能否组成一个完整连通图
        # 如否 返回-1 否则返回len(edges) - (n+x-2)
        for type, u, v in edges:
            if type == 1:
                if union(u, v, AliceUnion) : a += 1 # 如有新增就连通
            elif type == 2:
                if union(u, v, BobUnion) : b += 1
        

        if a < n-1 or b < n-1 : # 如果能连通，那么必有n-1条有效边
            return -1
        else :
            return len(edges) - (n+x-2)



print(Solution().maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
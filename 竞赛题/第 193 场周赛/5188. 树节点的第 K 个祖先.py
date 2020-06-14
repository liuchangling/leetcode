

# 5188. 树节点的第 K 个祖先
# 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。

# 请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。

# 树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。

 

# 示例：



# 输入：
# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

# 输出：
# [null,1,0,-1]

# 解释：
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

# treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
# treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
# treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
 

# 提示：

# 1 <= k <= n <= 5*10^4
# parent[0] == -1 表示编号为 0 的节点是根节点。
# 对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
# 0 <= node < n
# 至多查询 5*10^4 次

# 这道题乍一看是一个很简单的api题，实际上js可以通关
# 但python只用API会TLE。。。怎么做都TLE，做的想死
# 这个算法叫Binary Lifting ，本质其实是 dp。dp[node][j] 存储的是 node 节点距离为 2^j 的祖先是谁。
# 用一个额外的数组建立了2^j的祖先是谁

from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.data = [[-1 for i in range(n)] for j in range(16) ]

        for i, v in enumerate(parent):
            self.data[0][i] = v # 第一层父节点

        for j in range(1,16): # 分别代表第2层，第4层...第2^17层父节点
            for k in range(n):
                p = self.data[j-1][k]
                self.data[j][k] = self.data[j-1][p] if p>=0 else -1

        
        print(self.data)


    def getKthAncestor(self, node: int, k: int) -> int:
        p = node

        for i in range(15,-1,-1):
            if p < 0 : return -1

            if k & (1 << i):
                p = self.data[i][p]

        return p


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

o =  TreeAncestor(7,[-1,0,0,1,1,2,2])
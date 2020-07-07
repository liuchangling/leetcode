#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (54.26%)
# Likes:    475
# Dislikes: 0
# Total Accepted:    40.6K
# Total Submissions: 73.4K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 
# 找出路径和等于给定数值的路径总数。
# 
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
# 
# 示例：
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# 返回 3。和等于 8 的路径有:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # bfs 176ms 84%
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root : return 0

        # 为了方便，在root上添加了一个val=0的假根
        # 保存 节点，路径的前缀和，路径上的值
        queue = [(root,[0])] 
        ans = 0

        while queue: 
            node, preSum = queue.pop(0)

            total = node.val + preSum[-1] 

            for  pre in preSum:
                if total - pre == sum:
                    ans += 1
            
            newSum = preSum + [total]
            
            if node.left is not None : queue.append((node.left, newSum))
            if node.right is not None : queue.append((node.right, newSum))

        
        return ans

        # dfs 67.8% 256ms
#    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         global ans
#         ans = 0

#         def dfs(node:TreeNode, preSum: List[int]) -> int:
#             global ans
#             if node is None : return False

#             total = preSum[-1] + node.val
#             for p in preSum:
#                 if total - p == sum: ans += 1

#             newSum = preSum + [total]


#             dfs(node.left, newSum)
#             dfs(node.right, newSum)


#         dfs(root, [0])

#         return ans
# @lc code=end


# 求出路径版本
# class Solution:
#     # bfs
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         if not root : return []

#         # 为了方便，在root上添加了一个val=0的假根
#         # 保存 节点，路径的前缀和，路径上的值
#         queue = [(root,[0],[0])] 
#         ans = []

#         while queue: 
#             node, preSum, prePath = queue.pop(0)
#             print(node.val, preSum, prePath)

#             newPath = prePath + [node.val]

#             total = node.val + preSum[-1] 

#             for idx, pre in enumerate(preSum):
#                 if total - pre == sum:
#                     # 0~idx = pre 0~curIdx = total
#                     # total - pre == sum -> idx+1 ~ curIdx = sum
#                     ans.append(newPath[idx+1:])
#                     print(newPath[idx+1:])
            
#             newSum = preSum + [total]
#             print('after...',  newSum, newPath)
            
#             if node.left is not None : queue.append((node.left, newSum, newPath))
#             if node.right is not None : queue.append((node.right, newSum, newPath))

        
#         return ans        
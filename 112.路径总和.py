#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (49.15%)
# Likes:    352
# Dislikes: 0
# Total Accepted:    100.7K
# Total Submissions: 200.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
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
    # dfs 64ms 24%     
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:

    #     def dfs(node:TreeNode, count:int) -> int:
    #         if node is None : return False

    #         count += node.val
    #         if node.left is None and node.right is None:
    #             return count == sum

    #         return dfs(node.left, count) or dfs(node.right, count)


    #     return dfs(root, 0)

    # 52ms 81%
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root : return False
        if root.left is None and root.right is None: return root.val == sum

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # bfs  84ms 26%
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     queue = [(root,0)]

    #     while queue: 
    #         node, count = queue.pop(0)

    #         if node is None: continue
    #         count += node.val
    #         if node.left is None and node.right is None:
    #             if count == sum: 
    #                 return True
            
    #         queue.append((node.left, count))
    #         queue.append((node.right, count))

        
    #     return False
# @lc code=end

# js
# var hasPathSum = function (root, targetSum) {
#     let ret = false

#     function dfs(node, currentSum) {
#         if (!node) return

#         currentSum += node.val

#         if (node.left || node.right) {
#             dfs(node.left, currentSum)
#             dfs(node.right, currentSum)
#         } else {
#             if (currentSum === targetSum) {
#                 ret = true
#                 return
#             }
#         }
#     }


#     dfs(root, 0)
#     return ret

# };


# 简化版
# var hasPathSum = function (root, targetSum) {

#     function dfs(node, currentSum) {
#         if (!node) return false
#         currentSum += node.val

#         if (!node.left && !node.right) {
#             return currentSum === targetSum
#         } else {
#           return dfs(node.left, currentSum) || dfs(node.right, currentSum)
#         }
#     }


#     return dfs(root, 0)

# };
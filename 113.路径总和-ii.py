#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (58.92%)
# Likes:    264
# Dislikes: 0
# Total Accepted:    56.5K
# Total Submissions: 93.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    # dfs 60ms 19%
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []

        def dfs(node:TreeNode, count:int, path: List[int]) -> int:
            if node is None : return False

            count += node.val
            newPath = path + [node.val]
            if node.left is None and node.right is None:
                if count == sum:
                    ans.append(newPath[1:])


            dfs(node.left, count, newPath)
            dfs(node.right, count, newPath)


        dfs(root, 0, [0])

        return ans
    # bfs 84ms 5%
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    #     if not root : return []

    #     # 为了方便，在root上添加了一个val=0的假根
    #     # 保存 节点，路径的前缀和，路径上的值
    #     queue = [(root, 0, [0])] 
    #     ans = []

    #     while queue: 
    #         node, preSum, prePath = queue.pop(0)

    #         newPath = prePath + [node.val]

    #         preSum += node.val 

    #         if preSum == sum and node.left is None and node.right is None:
    #             ans.append(newPath[1:])
            
    #         if node.left is not None : queue.append((node.left, preSum, newPath))
    #         if node.right is not None : queue.append((node.right, preSum, newPath))

        
    #     return ans
# @lc code=end



# var pathSum = function (root, targetSum) {
#     let ret = []

#     function dfs(node, currentSum, path) {
#         if (!node) return false
#         currentSum += node.val
#         let newPath = path.concat(node.val)

#         if (!node.left && !node.right) {
#             if (currentSum === targetSum) {
#                 ret.push(newPath)
#             }
#         } else {
#             dfs(node.left, currentSum, newPath)
#             dfs(node.right, currentSum, newPath)
#         }
#     }


#     dfs(root, 0, [])
#     return ret

# };
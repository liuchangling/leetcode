#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (71.29%)
# Likes:    450
# Dislikes: 0
# Total Accepted:    121.9K
# Total Submissions: 169.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TreeNode{val: 3, left: None, right: None}

# 第一种思路就深度优先，然后记录最大深度返回,递归遍历如果存在的左右子树
# 实测速度92% 看起来不错。

# 有优化版写成一行的

# 第二种思路是非递归版本，通过堆栈或者队列实现。较繁琐这里不写了。

class Solution:
    # 思路1
    # def maxDepth(self, root: TreeNode) -> int:
    #     ret = 0
    #     if root:
    #         ret = ret + 1
    #         if root.left and root.right:
    #             return ret + max(self.maxDepth(root.left), self.maxDepth(root.right))
    #         elif root.left:
    #             return ret + self.maxDepth(root.left)
    #         elif root.right:
    #             return ret + self.maxDepth(root.right)
    #         else:
    #             return ret
    #     else:
    #         return ret

    # 写法优化一下
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

        
# @lc code=end


# js bfs
# var maxDepth = function(root) {
#     let queue = [root]
#     let deep = 0

#     while(queue.length>0){
#         deep ++
#         let temp = []
#         queue.forEach(q=>{
#             q && temp.push(q.left, q.right)
#         })
#         queue = temp
#     }

#     return deep
# };

# 递归简单点
# var maxDepth = function (root) {
#     if (!root) return 0
#     if (!root.left && !root.right) return 1  #这一行不需要，速度更快

#     return 1 + Math.max(maxDepth(root.left), maxDepth(root.right))
# };

 
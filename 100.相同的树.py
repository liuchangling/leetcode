#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (57.65%)
# Likes:    440
# Dislikes: 0
# Total Accepted:    126.1K
# Total Submissions: 211K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if p and not q:
            return False
        if not p and q:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        
# @lc code=end

# js递归
# var isSameTree = function(p, q) {
#     if(!p && !q) return true

#     if(p && q ){
#         return  p.val=== q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
#     }else{
#         return false
#     }

# };


# js非递归
# var isSameTree = function (p, q) {
#     let l = [p]
#     let r = [q]
#     while (l.length > 0) {
#         let newL = []
#         let newR = []
#         for (let i = 0; i < l.length; i++) {
#             if ((l[i] && !r[i]) || (r[i] && !l[i])) {
#                 return false
#             } else if (!r[i] && !l[i]) {
#             } else if (l[i] && r[i]) {
#                 if (l[i].val !== r[i].val) {
#                     return false
#                 } else {
#                     newL.push(l[i].left)
#                     newL.push(l[i].right)
#                     newR.push(r[i].left)
#                     newR.push(r[i].right)
#                 }
#             }
#         }
#         l = newL
#         r = newR
#     }
#     return true
# };
#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (51.07%)
# Likes:    800
# Dislikes: 0
# Total Accepted:    150K
# Total Submissions: 289.3K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
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
    # 迭代 bfs 68%
    # def isSymmetric(self, root: TreeNode) -> bool:

    #     if root is None:
    #         return True

    #     def check(nums):
    #         size = len(nums)
    #         for i in range( size // 2) :
    #             if nums[i] != nums[size - 1 -i]:
    #                 return False
            
    #         return True


    #     que = [root]
    #     val = [root.val]

    #     while len(que) > 0:
    #         if not check(val):
    #             return False

    #         n = []
    #         newVal = []
    #         for r in que:
    #             if r.left : 
    #                 n.append(r.left)
    #                 newVal.append(r.left.val)
    #             else:
    #                 newVal.append(None)

    #             if r.right : 
    #                 n.append(r.right)
    #                 newVal.append(r.right.val)
    #             else:
    #                 newVal.append(None)
                
    #             val = newVal
                
                

    #         que = n

    #     return True

    # 递归 95%
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(a: TreeNode, b:TreeNode) -> bool:
            if a is None and b is None: return True
            
            if a is None or b is None: return False
            
            # 注意对称是左和右比，右和左比
            return a.val == b.val and check(a.left, b.right) and check(a.right, b.left)

        
        return check(root, root)

    # 迭代 30%
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def check(a: TreeNode, b:TreeNode) -> bool:
    #         que = [a,b]
    #         while len(que) > 0:
              
    #             l = que.pop()
    #             r = que.pop()

    #             if l is None and r is None: continue
    #             if l is None or r is None: return False

    #             if l.val != r.val: return False

    #             que = [l.left, r.right , l.right, r.left] + que
            
    #         return True

    #     return check(root, root)

# @lc code=end


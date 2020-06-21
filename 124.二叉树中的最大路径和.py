#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (40.32%)
# Likes:    504
# Dislikes: 0
# Total Accepted:    45K
# Total Submissions: 109.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出: 6
# 
# 
# 示例 2:
# 
# 输入: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出: 42
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归判断每个节点的 自己加上[左子树最大值，右子树最大值，左右子树之和]的最大值，并更新全局最大值
# 子节点遇到负数可以舍弃。
# 然后递归向上更新全部节点即可

# 思路1 和思路2的区别是是否实现了舍弃节点的判断。 思路2无需判断节点为负数的情况，全部基于实际更新值计算。

class Solution:
    # 思路1，包含了舍弃节点的max(0,getMax)
    # def __init__(self):
    #     self.global_max = float('-inf')


    # def maxPathSum(self, root: TreeNode) -> int:

    #     def getMax(node: TreeNode) -> int:
    #         global global_max
    #         if node is None : return 0

    #         left = max(0, getMax(node.left))
    #         right = max(0, getMax(node.right))

    #         useNodePath = left + right + node.val

    #         self.global_max = max(self.global_max, useNodePath)

    #         return node.val + max(left, right) # 必须选用当前节点

    #     getMax(root)
        
    #     return self.global_max

    # 思路2 不做舍弃节点处理 代码节点一点
    def maxPathSum(self, root: TreeNode) -> int:
        res = [float("-inf")]
        
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            tmp = max(root.val+l, root.val+r, root.val)
            res[0] = max(res[0], tmp, root.val+l+r)
            return tmp
        
        dfs(root)
        return res[0]
        

# @lc code=end


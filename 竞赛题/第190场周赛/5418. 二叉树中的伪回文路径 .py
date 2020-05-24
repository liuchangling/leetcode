# 5418. 二叉树中的伪回文路径 
# 题目难度Medium
# 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

# 请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs全排列,当路径上每个字符出现次数均为奇数时，就说明有回文路径。
import collections
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.dfs(root, [])        


    def dfs(self, root: TreeNode, parentVals):
        vals = parentVals + [root.val]
        if root.left == None and root.right == None:
            c = collections.Counter(vals)
            firstOdd = False
            for value in c.values():
                if value % 2 == 1:
                    if not firstOdd:
                        firstOdd = True
                    else :
                        return 0

            return 1
        else :           
            left =  0 if root.left == None else self.dfs(root.left, vals) 
            right = 0 if root.right == None else self.dfs(root.right, vals)
            return left + right
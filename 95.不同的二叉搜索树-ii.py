#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (62.69%)
# Likes:    466
# Dislikes: 0
# Total Accepted:    36.7K
# Total Submissions: 57.9K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
# 
# 
# 
# 示例：
# 
# 输入：3
# 输出：
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 8
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


# 思路是一样的，不过这个代码实现我居然没有写出来。。。
# 这个代码写的就很酷，我开始以为push进去的是List， 实际上只需要push根节点进ans即可

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def createTree(start:int, end:int) -> List[TreeNode]:
            if start > end: return [None]

            all_trees = []

            for i in range(start, end + 1):
                left_trees = createTree(start, i-1)
                right_trees = createTree(i+1, end)

                for l in left_trees:
                    for r in right_trees:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        all_trees.append(cur)
            
            return all_trees


        

        return createTree(1,n) if n else []


        
# @lc code=end


#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (69.46%)
# Likes:    480
# Dislikes: 0
# Total Accepted:    87.5K
# Total Submissions: 120.3K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定有序数组: [-10,-3,0,5,9],
# 
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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


# 思路1 类似2分查找的感觉， 递归构造就完事了  60 ms 62%

# 思路2 没有辅助函数，优雅的递归 时间一样  60ms 62%

class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     if not nums: return None
        
    #     size = len(nums)
    #     def split(start, end):
    #         if start == end :
    #             return TreeNode(nums[start]) if start < size else TreeNode(None)

    #         if start + 1 == end :
    #             node = TreeNode(nums[end])
    #             node.left = TreeNode(nums[start])
    #             return node

    #         mid = (start+end)//2

    #         node = TreeNode(nums[mid]) 
            
    #         node.left = split(start,mid-1)
    #         node.right = split(mid+1, end)

    #         return node

    #     return split(0, size-1)



    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        # 选取中间的点，如果是偶数就右边的
        index = len(nums) // 2
        p = TreeNode(nums[index])
        # 递归调用
        p.left = self.sortedArrayToBST(nums[:index])
        p.right = self.sortedArrayToBST(nums[index+1:])
        return p
# @lc code=end



# var sortedArrayToBST = function(nums) {

#     function buildTree(low, high){
#         if(low>high) return null

#         let mid = Math.floor((low + high)/2)
#         let root = new TreeNode(nums[mid])
#         root.left = buildTree(low, mid-1)
#         root.right = buildTree(mid+1, high)
        
#         return root
#     }

#     return buildTree(0, nums.length-1)
# };
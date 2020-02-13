#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (66.54%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    34.9K
# Total Submissions: 51K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
# 
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
# 
# 示例 1:
# 
# 输入: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# 输出: 1
# 
# 示例 2:
# 
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# 输出: 3
# 
# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法1  bfs的中序遍历为升序数组 再取第k小就行了。这样速度在75%
# 方法2  找到就停止 不需要遍历整个树。把1中的递归改成迭代写法即可（借用堆栈,栈的作用是记录parent是谁）


class Solution:   
    # 方法1
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     def inorder(r: TreeNode) :
    #         # 中序遍历
    #         return inorder(r.left) + [r.val] + inorder(r.right) if r else []

    #     return inorder(root)[k-1]

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                # 查找最左子节点
                root = root.left
            root = stack.pop()

            k -= 1
            if not k:
                return root.val
            
            # 查找右子树
            root = root.right

    
        
# @lc code=end


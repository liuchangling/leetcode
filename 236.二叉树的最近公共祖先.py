#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (60.14%)
# Likes:    587
# Dislikes: 0
# Total Accepted:    86.7K
# Total Submissions: 135.8K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 
# 
# 示例 2:
# 
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 
# 
# 说明:
# 
# 
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
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

# 思路1 递归 56%
# 递归dfs，返回是否包含p，是否包含q，然后做一个加总
# 因为先做了337， 这个就很简单了。时间复杂度是o(n)
# 改成global ans 44%
#
# 思路2 递归 71%
#  发现官方题解方法差不多，不过递归时只返回一个值，代表是否包含p or q. 将我的思路2个值变成了1个
#  条件变成了，左右子树都有，或者自己本身是。且子树中也有。  return l or r or root.val in v


# 思路3 构造hash，向上遍历
# 先遍历树，构造一个hash，key是val， value指向父节点
# 然后p先走一次从叶到根，q再走一次，遇到已经走过的直接返回。
# 这个思路终于让我明白了如何获取父节点。个人觉得这个思路是最清晰的，但也需要额外空间


# 思路4 92%
# 高手在民间系列。。 代码特别简洁。
# 对一个节点来说，为空或者匹配到了pq就返回当前节点。这也是递归的终止条件
# 其他情况一定是非pq的值， 我们需要递归处理其左右子树
# 如果有None ，代表改子树中不含p，q。 直接return另一边，如left为空就返回right
# 如果左右都不是None， 说明找到了公共祖先。代码很漂亮


class Solution:
    # 思路1
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def _v(root: TreeNode):
        #     if root is None:
        #         return [False, False, None]
            
        #     l = _v(root.left)
        #     r = _v(root.right)

        #     if root.val == p.val:
        #         l[0] = True
        #         r[0] = True
        #     elif root.val == q.val:
        #         l[1] = True
        #         r[1] = True

        #     hasP = l[0] or r[0]
        #     hasQ = l[1] or r[1]
        #     ans = None

        #     if hasP and hasQ:
        #         ans = l[2] or r[2] or root

        #     return [hasP, hasQ, ans]
        
        # return _v(root)[2]

    # 思路1
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     global ans
    #     ans = None

    #     def dfs(root: TreeNode):
    #         global ans

    #         if root is None:
    #             return [False, False]
            
    #         l = dfs(root.left)
    #         r = dfs(root.right)

    #         if root.val == p.val:
    #             l[0] = True
    #             r[0] = True
    #         elif root.val == q.val:
    #             l[1] = True
    #             r[1] = True

    #         hasP = l[0] or r[0]
    #         hasQ = l[1] or r[1]

    #         if hasP and hasQ and ans is None:
    #             ans = root

    #         return [hasP, hasQ]
        
    #     dfs(root)

    #     return ans

    # 思路2 71%
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     global ans
    #     v = [p.val, q.val]
    #     def dfs(root: TreeNode):
    #         global ans
    #         if root is None: return False

    #         l = dfs(root.left)
    #         r = dfs(root.right)

    #         if l and r : ans = root
    #         if root.val in v and (l or r): ans = root

    #         return l or r or root.val in v
        
    #     dfs(root)

    #     return ans

    # 思路3 71%
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     hash = {}

    #     def dfs(root:TreeNode):
    #         if root is None: return
    #         if root.left : 
    #             hash[root.left.val] = root
    #             dfs(root.left)
    #         if root.right : 
    #             hash[root.right.val] = root
    #             dfs(root.right)

    #     dfs(root)

    #     visited = set()

    #     while p:
    #         visited.add(p.val)
    #         p = hash.get(p.val)
        
    #     while q:
    #         if q.val in visited : return q
    #         q = hash.get(q.val)


    # 思路4 92%
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == q or root == p: return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left: return right
        if not right: return left

        return root
        
# @lc code=end



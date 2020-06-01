#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (56.00%)
# Likes:    346
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 52.6K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \
# ⁠    3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
#     3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \
# ⁠1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
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

# 直觉要么就bfs走一波， 得到数组后然后在调用198呗
# 但这个是错的，[2,1,3,null,4] 可能会出现相邻两层都选用。父不用，然后用左孙+右儿
# 然后就发现难点了。。。如何对bfs进行dp呢

# 方案1 最优子结构定义为，当前节点能获取到的最大值
#       可以分为选用当前节点，和弃用当前节点两种情况，
#       进行递归计算即可。 思路正确， 但结果TLE

# 方案2 加了一个缓存，有一点优化，但仍然会TLE

# 方案3 每个节点存储两个值，保存偷和不偷的最大值。这样每个节点都只计算了一次。 超越97%

class Solution:
    # 思路1 结果正确，但TLE
    # def rob(self, root: TreeNode) -> int:
    #     if root is None :
    #         return 0

    #     cur = root.val

    #     # 选用当前节点，则加上4个孙子
    #     if root.left:
    #         cur += self.rob(root.left.left)
    #         cur += self.rob(root.left.right)
    #     if root.right:
    #         cur += self.rob(root.right.left)
    #         cur += self.rob(root.right.right)

    #     # 弃用当前节点，则加上左右子树的最大值（涵盖了左儿子加右孙子的情况）
    #     return max(cur, self.rob(root.left) + self.rob(root.right))

    # 思路2 加了一个memo缓存
    # def rob(self, root: TreeNode) -> int:

    #     memo = {}

    #     def _rob(root):
    #         if root is None :
    #             return 0

    #         if root in memo : return memo[root]

    #         cur = root.val

    #         # 选用当前节点，则加上4个孙子
    #         if root.left:
    #             cur += self.rob(root.left.left)
    #             cur += self.rob(root.left.right)
    #         if root.right:
    #             cur += self.rob(root.right.left)
    #             cur += self.rob(root.right.right)

    #         # 弃用当前节点，则加上左右子树的最大值（涵盖了左儿子加右孙子的情况）
    #         ans = max(cur, self.rob(root.left) + self.rob(root.right))
    #         memo[root] = ans

    #         return ans

    #     return _rob(root)

    def rob(self, root: TreeNode) -> int:
        # 用了， 没用
        def _rob(root: TreeNode):
            if root is None:
                return [0, 0]
            # 用了当前节点，下一层只能选未用
            l = _rob(root.left)
            r = _rob(root.right)
            used = l[1] + r[1] + root.val

            # 没用当前节点  下一层可以用，也可以不用。选最大值即可
            unused = max(l[0], l[1]) + max(r[0], r[1])

            return [used, unused]

        return max(_rob(root))


# @lc code=end

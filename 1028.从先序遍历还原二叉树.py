#
# @lc app=leetcode.cn id=1028 lang=python3
#
# [1028] 从先序遍历还原二叉树
#
# https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/description/
#
# algorithms
# Hard (61.69%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    13.1K
# Total Submissions: 17.8K
# Testcase Example:  '"1-2--3--4-5--6--7"'
#
# 我们从二叉树的根节点 root 开始进行深度优先搜索。
# 
# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D +
# 1。根节点的深度为 0）。
# 
# 如果节点只有一个子节点，那么保证该子节点为左子节点。
# 
# 给出遍历输出 S，还原树并返回其根节点 root。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入："1-2--3--4-5--6--7"
# 输出：[1,2,5,3,4,6,7]
# 
# 
# 示例 2：
# 
# 
# 
# 输入："1-2--3---4-5--6---7"
# 输出：[1,2,5,3,null,6,null,4,null,7]
# 
# 
# 示例 3：
# 
# 
# 
# 输入："1-401--349---90--88"
# 输出：[1,401,null,349,88,90]
# 
# 
# 
# 
# 提示：
# 
# 
# 原始树中的节点数介于 1 和 1000 之间。
# 每个节点的值介于 1 和 10 ^ 9 之间。
# 
# 
# 我发现我写反序列化很薄弱。。。这个题思想讲解起来没有图不好弄，直接戳下面链接吧
# 遍历时知道节点的值number和深度level
# 1. 根节点无条件入栈，不操作，也不出栈
# 2. 如果len(stack) > level 就一直出栈直到两者相等，进入3.
# 3. 当level等于len(stack), stack[-1]必然是当前节点的父节点，这个看题解的图比较清楚
# 4. 已经直到stack[-1]是父节点，当前节点插入位置能左就左，不能就右
# 5. 最后把当前节点入栈

# 链接：https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/shou-hui-tu-jie-fei-di-gui-fa-zhong-gou-chu-er-cha/

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        size = len(S)
        i = 0 

        stack = []

        while i < size:
            level = 0 
            # ----
            while S[i] == '-':
                level += 1
                i += 1
            # digit
            number = 0 
            while i < size and S[i].isdigit():                
                number = number * 10 + int(S[i])
                i += 1

            cur = TreeNode(number)
            if len(stack) == 0 : 
                stack.append(cur)
            else:
                while len(stack) > level:
                    # 栈底元素不是父亲，就一直出栈找爸爸
                    stack.pop()
                if stack[-1].left :
                    # 左儿子存在，则安排为右儿子
                    stack[-1].right = cur
                else:
                    # 否则安排为左儿子
                    stack[-1].left = cur

                # 最后入栈
                stack.append(cur)
        
        return stack[0]

        
# @lc code=end
# Solution().recoverFromPreorder("1-2--3---4-5--6---7")

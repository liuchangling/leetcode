#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路1 递归 超越78%
# 前序 根 + 左子树 + 右子树
# 中序 左子树 + 根 + 右子树
# 可以看出前序中第一个就是根root
# 在中序中找到root对应位置，就可以知道左子树和右子树的长度。
# 递归处理左右子树的前序和中序
#  
# 思路2 递归优化 97%
# 注意到反复通过下标找寻中序次数较多，可以先遍历一次中序，转成散列表。后续查找只需要o(1)的时间
#   
# 思路3 是一个迭代版本，比较麻烦，证明较繁琐，懒得写了


class Solution:
    # 思路1 78%
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     size = len(preorder)

    #     if size == 0:
    #         return None
    #     elif size == 1: # 叶节点直接返回
    #         return TreeNode(preorder[0])


    #     val = preorder[0]
    #     ans = TreeNode(val)
    #     root = inorder.index(val)        

    #     ans.left = self.buildTree(preorder[1: 1+root], inorder[0: root])
    #     ans.right = self.buildTree(preorder[root+1: ], inorder[root + 1: ])

    #     return ans

    # 思路2  97%
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder) - 1
        m = {element: i for i, element in enumerate(inorder)} # 精简的list 转 dict


        def findTree(pL: int, pR:int, iL:int, iR:int ):
            if pL > pR:
                return None

            ans = TreeNode(preorder[pL])

            root = m[preorder[pL]]
            subLeftPR = pL  + (root - iL)

            ans.left = findTree(pL+1, subLeftPR, iL, root-1)
            ans.right = findTree(subLeftPR+1, pR, root+1,iR)

            return ans
        
        return findTree(0,n,0,n)

# @lc code=end


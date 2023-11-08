#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (65.54%)
# Likes:    680
# Dislikes: 0
# Total Accepted:    67.3K
# Total Submissions: 98.4K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 思路1 dp
# 这道题的dp是真的有点难想。
# 正确的思考回路是，我们先从问题看，要得到G(n) = n个节点的二叉搜索树总数(0~n-1)
# 定义F(i,n)为以i为根的二叉搜索树总数。那么G(n) = F(0,n) + F(1,n)+ ...+F(n-1,n)
# 再看F(i,n) 左子树为0~i-1 右子树为i+1~n-1 所以F(i,n) = G(i) * G(n-i-1)
# 注意到这个拆分 就意味着该问题是可以拆分为子问题处理的。就可以用dp了
# G(n) = sum(G(i)*G(n-i-1)) (i in range(n))

# 思路2 卡塔兰数
# 思路1可以简化为数学递推式
# G(n+1) = 2(2n+1)G(n) / (n+2)
# G(n) = 2(2n-1)G(n-1) / (n+1)

from functools import lru_cache

# @lc code=start
class Solution:

    # dp 44ms 41%
    # @lru_cache(None)
    # def numTrees(self, n: int) -> int:
    #     if n <= 1 : return 1
    #     ans = 0
    #     for i in range(n):
    #         ans += self.numTrees(i) * self.numTrees(n-i-1)
        
    #     return ans

    # 数学法 40ms 65%
    def numTrees(self, n: int) -> int:
        if n <= 1 : return 1
        return int(2*(2*n-1) * self.numTrees(n-1) / (n+1))

# @lc code=end

# var numTrees = function(n) {
# 	let g = [1]
# 	for(let i = 1; i <= n ; i++){
# 		g[i] = 0
# 		for(let j = 0; j < i; j++){
# 			g[i] += g[j]*g[i-j-1]
# 		}
# 	}
# 	return g[n]
# };
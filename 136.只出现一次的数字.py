#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (64.01%)
# Likes:    1062
# Dislikes: 0
# Total Accepted:    149.1K
# Total Submissions: 228.4K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
# 额。。本身很简单，但是要O(n)又不让额外空间就很难想了。。。
# 
# 思路1 数学法 原理是 2∗(a+b+c)−(a+a+b+b+c)=c 但还是借用了额外空间 只是好玩而已。速度13%
# 思路2 位运算 原理是 a^b^a = a^a^b = 0^b
# 如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
# 如果我们对相同的二进制位做 XOR 运算，返回的结果是 0
# XOR 满足交换律和结合律
# 

# @lc code=start
class Solution:
    # 思路1 
    # def singleNumber(self, nums: List[int]) -> int:
    #     return sum(set(nums)) * 2 - sum(nums)

    # 思路2
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        
        return a
        
# @lc code=end


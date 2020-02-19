#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (50.55%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    109.7K
# Total Submissions: 212.6K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
# 
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: true
# 
# 示例 2:
# 
# 输入: [1,2,3,4]
# 输出: false
# 
# 示例 3:
# 
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
# 
# 思路1 借用set 实际速度仅击败了 5%。问题应该是出现在频繁add操作上，
#      导致时间复杂度较高
#
# 思路2 转成set 实际上因为add操作少，击败93%。。。比1还快点


from typing import List
# @lc code=start
class Solution:
    #  思路1
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     m = set()
    #     for i in nums:
    #         if i in m:
    #             return True
    #         else :
    #             m.add(i)
        
    #     return False

    # 思路2
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
        
# @lc code=end


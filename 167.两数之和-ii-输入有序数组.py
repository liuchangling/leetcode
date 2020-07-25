#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (53.82%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    133.4K
# Total Submissions: 237.8K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
# 
# 说明:
# 
# 
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 
# 
# 示例:
# 
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
# 
#

# @lc code=start
class Solution:
    # 第一题的hash思路 40ms 90%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {} # 使用hashmap进行一次遍历
        for index, value in enumerate(numbers):
            # 找到个合适的就返回
            if value in m :
                return [m[value] + 1 , index + 1]
            # 没找到时，将target-value 和index存入map
            else :
                m[target-value] = index

    # 左右指针 44ms 75% 实际比第一种慢诶
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     l = 0 
    #     r = len(numbers)-1

    #     while l <= r:
    #         cur = numbers[l] + numbers[r]

    #         if cur == target:
    #             return [l+1, r+1]
    #         elif cur > target:
    #             r -= 1
    #         else:
    #             l += 1

            

# @lc code=end


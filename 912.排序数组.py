#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (51.42%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    15.9K
# Total Submissions: 30.2K
# Testcase Example:  '[5,2,3,1]'
#
# 给定一个整数数组 nums，将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：[5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# -50000 <= A[i] <= 50000
# 
# 没什么好解释的 你懂得 
# 1. 冒泡 运行结果是超时
#


from typing import List
# @lc code=start
class Solution:
    # 冒泡  会超时 优化思路：记录上一次交换位置后续不用再移动
    # def sortArray(self, nums: List[int]) -> List[int]:        
    #     length = len(nums)
    #     for i in range(length - 1):
    #         for j in range(0, length - i - 1):
    #             if nums[j] > nums[j+1]:
    #                 t = nums[j]
    #                 nums[j] = nums[j+1]
    #                 nums[j+1] = t

    #     return nums

    # 选择排序，每次找到最小的，和当前节点交换 寻找[i, n)区间里的最小值的索引
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     length = len(nums)
    #     for i in range(length - 1):
    #         m = nums[i]
    #         temp = i 
    #         for j in range(i + 1, length):
    #             if m > nums[j] :
    #                 temp = j 
    #                 m = nums[j]

    #         nums[temp] = nums[i]
    #         nums[i] = m
        
    #     return nums

    # 插入排序， 每次插到前面数组中合适的位置
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     length = len(nums)
    #     for i in range(1, length):
    #         t = nums[i]
    #         temp = 0
    #         for j in reversed(range(0, i)):
    #             if nums[j] > t :
    #                 nums[j+1] = nums[j]
    #             else :
    #                 temp = j + 1
    #                 break
            
    #         nums[temp] = t

    #     return nums

    # 快速排序
    # def sortArray(self, nums: List[int]) -> List[int]: 

# print(Solution().sortArray([5,2,3,1]))
# @lc code=end


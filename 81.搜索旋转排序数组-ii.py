#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (35.14%)
# Likes:    149
# Dislikes: 0
# Total Accepted:    26.5K
# Total Submissions: 74.6K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
# 
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
# 
# 示例 1:
# 
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
# 
# 进阶:
# 
# 
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
# 
# 思路1 api in 超越81% 不会TLE
# 思路2 仿33题 特殊处理nums[l] == nums[h] 的情况 也是81%

# from typing import List
# @lc code=start
class Solution:
    # return target in nums

    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        h = len(nums) - 1

        while l <= h :
            mid = (l + h) // 2

            x = nums[mid]

            if target == x or nums[l] == target or nums[h] == target:
                return True
            elif nums[l] == nums[h]:
                l += 1 
                h -= 1
            elif target < x: 
                if nums[l] <= x and nums[l] > target:
                    # 左有序 且左侧最小值比target大，那就在右边找
                    l = mid + 1
                else:
                    h = mid - 1
            else :
                # target > x
                if nums[h] >= x and nums[h] < target:
                    # 右有序 且右侧最大值比target小，那就在左边找
                    h = mid - 1
                else:
                    l = mid + 1
        
        return False

# @lc code=end

# print(Solution().search([2,5,6,0,0,1,2], 3))
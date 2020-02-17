#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.94%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    73.7K
# Total Submissions: 171.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# 思路1 类似15题，先排序，然后每次取一个元素，通过左右指针进行移动来计算最接近的值，这里处理提前结束条件稍微麻烦一点
# 

# @lc code=start
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        nearest = nums[0] + nums[1] + nums[2]
        minDis = abs(nearest - target)
        size = len(nums);

        for i in range(size - 2) :
            if i > 0 and nums[i] == nums[i-1]:
                # 之前算过的话提前退出
                continue

                
            l = i + 1
            r = size - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                distance = sum - target
                if distance == 0: 
                    return target
                elif distance > 0:                    
                    r -= 1
                else:
                    l += 1
                
                if abs(distance) < minDis:
                    minDis = abs(distance)
                    nearest = sum

        return nearest    

# print(Solution().threeSumClosest([-1,2,1,-4], 1))

        
# @lc code=end
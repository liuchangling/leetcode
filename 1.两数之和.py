#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # 使用hashmap进行一次遍历
        for index, value in enumerate(nums):
            # 找到个合适的就返回
            if value in m :
                return [m[value], index]
            # 没找到时，将target-value 和index存入map
            else :
                m[target-value] = index

# @lc code=end


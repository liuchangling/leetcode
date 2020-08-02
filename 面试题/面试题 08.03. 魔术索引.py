# 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

# 示例1:

#  输入：nums = [0, 2, 3, 4, 5]
#  输出：0
#  说明: 0下标的元素为0
# 示例2:

#  输入：nums = [1, 1, 1]
#  输出：1
# 说明:

# nums长度在[1, 1000000]之间
# 此题为原书中的 Follow-up，即数组中可能包含重复元素的版本

# 有序找下标，第一反应就是二分
# 猜答案是mid， 如果nums[mid] == mid 就 r = mid . 否则l = mid + 1
# 
from typing import List

class Solution:
    # 48 ms 50% 暴力法
    # def findMagicIndex(self, nums: List[int]) -> int:
    #     for idx, v in enumerate(nums):
    #         if idx == v :
    #             return idx

    #     return -1

    # 44ms 73%
    def findMagicIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == i:
                return i
            if nums[i] > i:  # 此时我们可以排除索引i到nums[i-1]这一整段
                i = nums[i]  # 由于数组可以保持平稳，所以nums[i]这一元素不可排除
            else:
                i += 1

        return -1

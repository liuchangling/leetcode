#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
# 嘿 说明还指出不能用除法。。。我第一反应就是乘一次，每个除一下
# 额。。写完了failed at [0,0]这个测试，算了，没必要特殊处理了，老老实实写。
# 暴力法，老老实实乘，算法复杂度O(n2),题目要求o(n)
# ---看了一波答案，挺有思想的
# 方法一：左右乘法
#        两次遍历，得到左边乘积数组left和右边乘积数组right
#        对于i 即为left[i] * right[len(num) -i]
# 这种算法时间复杂度为o(n)
# 进阶问题是空间复杂度要为1 
# 方法二：优化，即分别用左右指针记录左边乘积和右边乘积，并执行输出。。。

# @lc code=start
from typing import List
# from functools import reduce


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     l = len(nums) - 1
    #     left = [1] # i左侧乘积
    #     right = [1] # l - i 右侧乘积
    #     for i in range(l):
    #         left.append(left[i] * nums[i])
    #         right.append(right[i] * nums[l - i])

    #     ret = []
    #     for j in range(l + 1):
    #         ret.append(left[j] * right[l - j])

    #     return ret

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, l, r = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], l = res[i] * l, l * nums[i]
            res[j], r = res[j] * r, r * nums[j]
        return res


# @lc code=end

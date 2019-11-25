#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
# 第一反应联想到入坑第一题。当时解法是做一个dict映射
# 那么这种思想能否推广到3数呢？
# 思路1: 1-2，依次遍历每一个元素，对于后面的元素使用2sum算法？
#       时间复杂度  O(n^2)
#       空间复杂度  O(n)
# 实验了一下，
# 结果有一个长度为3000测试集报错Time Limit Exceeded。。。。我的天呐。。。
# 我把那个测试集放到/test/15.txt里面了。实际上按照方法1跑，要75s。。。


# @lc code=start
from typing import List


class Solution:
    # 思路1 Time Limit Exceeded。。。尴尬
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        handled = []
        for index, num in enumerate(nums):
            if num in handled:
                continue

            temp = []
            print(index)
            target = 0 - num
            hasFound = False
            for after in nums[index+1:]:
                if after in temp:
                    answer = [num, 0 - num - after, after]
                    answer.sort()
                    if answer not in result:
                        result.append(answer)
                        hasFound = True
                else:
                    temp.append(target - after)

            if hasFound:
                handled.append(num)
        return result

# print(Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))

# 超时的那个测试包含3000个数 要70s
with open('./test/15.txt', 'rt') as in_file:
    text = in_file.read()

a = text.split(',')
a = [int(i) for i in a]
print(Solution().threeSum(a))

# @lc code=end

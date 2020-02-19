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
# 
# 排序次数太多了，干脆整体排序一次吧
# 我们尝试将数组先进性一次排序试试。实际上排序不到0.1s。很快就结束了。。。
# 思路2 ： 速度88%
#     1. 先排序
#     2. 遍历 比如取出num，target-num
#     3. 从左至右search ,当相加超出目标值即可退出。
#     4. 跳过当前数字到下一个为止
# 总共下来1.4s 真是令人哭泣。。。惭愧的1b 打败了88%。 去重通过转字符串放到字典实现
# 将3的优化加入之后只需要0.7s了
# 思路3 网上解答以双指针为主。 速度25%左右。。
#     1. 先排序
#     2. 对于一个数，计算其target
#     3. low和high 相加和对比,  大于target ， low++， 小于target high--
# 思路3优化版 使用下标替代了set，提升到36.5% 依然不如思路2。 跑3000个要2.2s



# @lc code=start
from typing import List


class Solution:
    # 思路1 Time Limit Exceeded。。。尴尬
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     handled = []
    #     for index, num in enumerate(nums):
    #         if num in handled:
    #             continue

    #         temp = []
    #         print(index)
    #         target = -num
    #         hasFound = False
    #         for after in nums[index+1:]:
    #             if after in temp:
    #                 answer = [num, 0 - num - after, after]
    #                 answer.sort()
    #                 if answer not in result:
    #                     result.append(answer)
    #                     hasFound = True
    #             else:
    #                 temp.append(target - after)

    #         if hasFound:
    #             handled.append(num)
    #     return result

    # # 思路2: 先排序试试
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        handled = set()
        ret = set()

        for index, num in enumerate(nums):
            if num in handled:
                continue
            
            # 另外倆数和的目标值
            target = -num

            temp = set()
            for n in nums[index+1:]:
                # 在后续数组中找找
                if n in temp:
                    ret.add(str(num) + ';' + str(target - n) + ';' + str(n))
                    handled.add(num)
                elif target < n + nums[index+1]:
                    # 和最小的比都超出去了，就提前退掉
                    break
                else :
                    temp.add(target - n)

        ret_list = []
        for r in ret:
            answer = [int(n) for n in r.split(';')]
            ret_list.append(answer)
        return ret_list

    # 思路3
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) < 3 :
    #         return []
        
    #     nums.sort()
    #     last = len(nums) - 1

    #     ret = []
    #     handled = set()

    #     for index,num in enumerate(nums) :

    #         if num in handled:
    #             continue

    #         low = index + 1
    #         high = last
    #         target = -num

    #         temp = set()
    #         while low < high:
    #             if nums[low] in temp:
    #                 low += 1
    #                 continue
                
    #             elif nums[high] in temp:
    #                 high -= 1
    #                 continue

    #             if nums[low] + nums[high] == target:
    #                 handled.add(num)
    #                 ret.append([num, nums[low], nums[high]])
    #                 temp.add(nums[low])
    #                 temp.add(nums[high])
    #                 low += 1
    #                 high -= 1

    #             elif nums[low] + nums[high] > target:
    #                 high -= 1

    #             elif nums[low] + nums[high] < target:
    #                 low += 1

    #     return ret


    # 思路3优化版
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) < 3 :
    #         return []
        
    #     nums.sort()
    #     last = len(nums) - 1

    #     ret = []

    #     for index,num in enumerate(nums) :

    #         if index > 0 and num == nums[index - 1]:
    #             continue

    #         low = index + 1
    #         high = last
    #         target = -num

    #         while low < high:
    #             sum = nums[low] + nums[high]
    #             if low > index + 1 and nums[low] == nums[low - 1] :
    #                 low += 1
                
    #             elif high < last and nums[high] == nums[high + 1]:
    #                 high -= 1

    #             elif sum > target:
    #                 high -= 1

    #             elif sum < target:
    #                 low += 1

    #             else:
    #                 ret.append([num, nums[low], nums[high]])
    #                 low += 1
    #                 high -= 1

    #     return ret
# print(Solution().threeSum([0,0,0]))
#print(Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))

# 超时的测试包含3000个数,方法1要75s，方法2 0.7s

# @lc code=end

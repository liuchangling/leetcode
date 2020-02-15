#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (59.09%)
# Likes:    1119
# Dislikes: 0
# Total Accepted:    137.8K
# Total Submissions: 225.1K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 
# 
# 
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 
# 
# 
# 示例:
# 
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
# 
#

# @lc code=start


# 思路1，懒人思路：暴力破解法 O(n^2) 遍历一下，在返回最大面积即可。
# 有一个长度为5000的测试用例超时了，Time Limit Exceeded
# 本地跑需要6.2s。说明这个不符合他的时间复杂度要求。。
#
# 思路2， 如果我们从左右安排两个指针，
#    左端需要右移的情况，偏右位置存在某个比自己高，且计算面积比之前最大值大
#    右端需要左移的情况，偏左位置存在某个比自己高，且计算面积比之前最大值大
#  failed at  [2,3,4,5,18,17,6] 我算出16 实际答案是17
# 看了答案，思路2需要更改移动方式：将指向较短线段的指针向较长线段那端移动一步。
# 正确的思路2：
#   总是将较短的一端向较长的一端移动，一次遍历结束。 很奇怪的是 速度在55%。。。
# 优化，结合我自己的思路， 当数值变小直接跳过计算，前往下一步。速度提高到76%


from typing import List
class Solution:
    # 暴力法
    # def maxArea(self, height: List[int]) -> int:
    #     ret = 0
    #     size = len(height)
    #     print(size)
    #     for i in range(0, size):
    #         for j in range(i+1, size):
    #             temp = (j - i) * min(height[i], height[j])
    #             ret = max(temp, ret)
        
    #     print(ret)
    #     return ret

    # 思路2的错误解法
    # def maxArea(self, height: List[int]) -> int:
    #     l = 0 
    #     r = len(height) - 1
    #     lastHeight = min(height[l], height[r])
    #     ret = r * lastHeight

    #     toRight = True

    #     while l < r :
    #         if toRight:
    #             l = l + 1
    #         else :
    #             r = r -1 
            
    #         newHeight = min(height[l], height[r])
    #         if newHeight > lastHeight:
    #             ret = max(ret, (r-l) * newHeight)

    #     return ret


    # 思路2：
    # def maxArea(self, height: List[int]) -> int:
    #     l = 0 
    #     r = len(height) - 1
    #     lastHeight = min(height[l], height[r])
    #     ret = r * lastHeight

    #     while l < r :
    #         if height[l] < height[r]:
    #             l = l + 1
    #         else :
    #             r = r -1 
            
    #         newHeight = min(height[l], height[r])
    #         if newHeight > lastHeight:
    #             ret = max(ret, (r-l) * newHeight)

    #     return ret

    # 思路2 优化，当数值变小了直接下一步
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        ret = r * min(height[l], height[r])

        while l < r :
            if height[l] < height[r]:
                l = l + 1
                if height[l] <= height[l-1]:
                    continue
            else :
                r = r - 1 
                if height[r] <= height[r+1]:
                    continue
            
            ret = max(ret, (r-l) * min(height[l], height[r]))

        return ret


        
# @lc code=end

# Solution().maxArea([2,3,4,5,18,17,6])
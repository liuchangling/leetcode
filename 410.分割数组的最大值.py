#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
# https://leetcode-cn.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (42.67%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 20.4K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
# 
# 注意:
# 数组长度 n 满足以下条件:
# 
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 示例: 
# 
# 
# 输入:
# nums = [7,2,5,10,8]
# m = 2
# 
# 输出:
# 18
# 
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
# 
# 思路1 dp 6700ms
# dp[i][j] 表示前i个数切分为j段
# dp[0][1] = nums[0]
# dp[i][j] = min(max( dp[i-1][j-1], nums[i]), max(dp[i-2][j-1], nums[i-1:i+1])...)


# 思路2 贪心二分查找 44ms 83%
# 二分的上界为数组 \textit{nums}nums 中所有元素的和，下界为数组 \textit{nums}nums 中所有元素的最大值。通过二分查找，我们可以得到最小的最大分割子数组和，这样就可以得到最终的答案了。


# @lc code=start
class Solution:
    # 思路1 dp 6700ms
    # def splitArray(self, nums: List[int], m: int) -> int:

    #     n = len(nums)
    #     f = [[10**18] * (m + 1) for _ in range(n + 1)]
    #     sub = [0]
    #     for elem in nums:
    #         sub.append(sub[-1] + elem)
        
    #     f[0][0] = 0
    #     for i in range(1, n + 1):
    #         for j in range(1, min(i, m) + 1):
    #             for k in range(i):
    #                 f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        
    #     return f[n][m]


    # 贪心二分 44ms
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m


        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid): # 拆分个数小于m，调小猜测值，使得个数增加
                right = mid
            else:
                left = mid + 1

        return left



        
# @lc code=end


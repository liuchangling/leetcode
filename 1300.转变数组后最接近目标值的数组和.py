#
# @lc app=leetcode.cn id=1300 lang=python3
#
# [1300] 转变数组后最接近目标值的数组和
#
# https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/description/
#
# algorithms
# Medium (45.42%)
# Likes:    71
# Dislikes: 0
# Total Accepted:    11.2K
# Total Submissions: 24.1K
# Testcase Example:  '[4,9,3]\n10'
#
# 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value
# 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
# 
# 如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
# 
# 请注意，答案不一定是 arr 中的数字。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [4,9,3], target = 10
# 输出：3
# 解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
# 
# 
# 示例 2：
# 
# 输入：arr = [2,3,5], target = 10
# 输出：5
# 
# 
# 示例 3：
# 
# 输入：arr = [60864,25176,27249,21296,20204], target = 56803
# 输出：11361
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5
# 
# 思路1 二分查找，比较差值即可
# 思路2 先排序，辅助空间存储前缀和 然后计算方式为前n个 加 mid* (len(arr)-n) 这样进行二分查找
#       说明了一个问题，涉及求和求积的，经常会先存一个前缀和子数组
# 思路3 我们找到最接近target且小于等于target的small， 然后small+1 就是大于target中最接近target的
#       然后比较small和target的差值，返回即可


from typing import List
# @lc code=start
class Solution:
    # 思路1 200ms 
    # def findBestValue(self, arr: List[int], target: int) -> int:

    #     def check(mid:int)->int:
    #         count = 0
    #         for n in arr:
    #             count += min(n, mid)
    #         return count - target


    #     S,maxArr = sum(arr), max(arr)
    #     if S < target : return maxArr
        
    #     l = 0 
    #     r = maxArr

    #     diff = abs(S - target)
    #     ans = maxArr

    #     while l <= r :
    #         mid = (l+r) // 2
    #         tmp = check(mid)
    #         # print('mid, diff, tmp:', mid, diff, tmp)
    #         if abs(tmp) < diff:
    #             ans = mid
    #             diff = abs(tmp)
    #         elif abs(tmp) == diff:
    #             ans = min(ans, mid)

    #         if tmp < 0:
    #             l = mid + 1
    #         else:
    #             r = mid - 1


    #     return ans

    # 思路2  632ms
    # def findBestValue(self, arr: List[int], target: int) -> int:
    #     arr.sort()
    #     n = len(arr)
    #     prefix = [0]
    #     for num in arr:
    #         prefix.append(prefix[-1] + num)
        
    #     r, ans, diff = max(arr), 0, target
    #     for i in range(1, r + 1):
    #         it = bisect.bisect_left(arr, i)
    #         cur = prefix[it] + (n - it) * i
    #         if abs(cur - target) < diff:
    #             ans, diff = i, abs(cur - target)
    #     return ans

    # 思路3 68ms
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        
        l, r, ans = 0, max(arr), -1
        while l <= r:
            mid = (l + r) // 2
            it = bisect.bisect_left(arr, mid)
            cur = prefix[it] + (n - it) * mid
            if cur <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        def check(x):
            return sum(x if num >= x else num for num in arr)
        
        choose_small = check(ans)
        choose_big = check(ans + 1)
        return ans if abs(choose_small - target) <= abs(choose_big - target) else ans + 1

# @lc code=end


# print(Solution().findBestValue([60864,25176,27249,21296,20204], 56803))
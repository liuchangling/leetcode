# 给你一个整数数组 bloomDay，以及两个整数 m 和 k 。

# 现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。

# 花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。

# 请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。

#  

# 示例 1：

# 输入：bloomDay = [1,10,3,10,2], m = 3, k = 1
# 输出：3
# 解释：让我们一起观察这三天的花开过程，x 表示花开，而 _ 表示花还未开。
# 现在需要制作 3 束花，每束只需要 1 朵。
# 1 天后：[x, _, _, _, _]   // 只能制作 1 束花
# 2 天后：[x, _, _, _, x]   // 只能制作 2 束花
# 3 天后：[x, _, x, _, x]   // 可以制作 3 束花，答案为 3
# 示例 2：

# 输入：bloomDay = [1,10,3,10,2], m = 3, k = 2
# 输出：-1
# 解释：要制作 3 束花，每束需要 2 朵花，也就是一共需要 6 朵花。而花园中只有 5 朵花，无法满足制作要求，返回 -1 。
# 示例 3：

# 输入：bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# 输出：12
# 解释：要制作 2 束花，每束需要 3 朵。
# 花园在 7 天后和 12 天后的情况如下：
# 7 天后：[x, x, x, x, _, x, x]
# 可以用前 3 朵盛开的花制作第一束花。但不能使用后 3 朵盛开的花，因为它们不相邻。
# 12 天后：[x, x, x, x, x, x, x]
# 显然，我们可以用不同的方式制作两束花。
# 示例 4：

# 输入：bloomDay = [1000000000,1000000000], m = 1, k = 1
# 输出：1000000000
# 解释：需要等 1000000000 天才能采到花来制作花束
# 示例 5：

# 输入：bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
# 输出：9
#  

# 提示：

# bloomDay.length == n
# 1 <= n <= 10^5
# 1 <= bloomDay[i] <= 10^9
# 1 <= m <= 10^6
# 1 <= k <= n



# 二分查找答案 l = 0 r = max(bloomDay)
# k是一直要用的
# can(mid) >= m 往前找， r = mid-1
# can(mid) < m 往后找 l = mid + 1

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        size = len(bloomDay)

        
        # return 当前mid可以摘几朵
        def can(mid: int)->int:
            def check(start:int): # 返回值用了滑动窗口，如果false每次滑动1会TLE
                if start + k > size: return (False, size)

                for j in range(start, start+k):
                    if mid < bloomDay[j] :
                        return (False, j+1)
                return (True, start+k)

            i = 0 
            count = 0 
            while i < size:
                isValid , i = check(i)
                if isValid: count += 1
            return count


        l = 0
        r = max(bloomDay)

        ans = -1
        while l <= r:
            mid = (l+r) // 2 
            t = can(mid)
            
            if t == m:
                ans = mid
                r = mid -1
            elif t < m :
                l = mid + 1
            else:
                ans = min(mid, ans) if ans!=-1 else mid

                r = mid - 1

        return ans



print(Solution().minDays([1,10,3,10,2],3,1))



# 别人题解， 对于滑动窗口的问题进行了简化处理，直接计算遍历到当前位置，有多少个连续的大于等于mid的数字
# 然后对k进行整除即可
# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         l = 0
#         r = 1000000000
#         if m * k > len(bloomDay):
#             return -1
#         while l + 1 < r:
#             mid = (l + r) // 2
#             cnt = 0
#             mm = 0
#             for i in range(len(bloomDay)):
#                 if bloomDay[i] <= mid:
#                     cnt += 1
#                 else:
#                     mm += cnt // k
#                     cnt = 0
#             mm += cnt // k
#             if mm >= m:
#                 r = mid
#             else:
#                 l = mid
#         return r

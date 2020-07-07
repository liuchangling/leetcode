# LCP 08. 剧情触发时间
# 在战略游戏中，玩家往往需要发展自己的势力来触发各种新的剧情。一个势力的主要属性有三种，分别是文明等级（C），资源储备（R）以及人口数量（H）。在游戏开始时（第 0 天），三种属性的值均为 0。

# 随着游戏进程的进行，每一天玩家的三种属性都会对应增加，我们用一个二维数组 increase 来表示每天的增加情况。这个二维数组的每个元素是一个长度为 3 的一维数组，例如 [[1,2,1],[3,4,2]] 表示第一天三种属性分别增加 1,2,1 而第二天分别增加 3,4,2。

# 所有剧情的触发条件也用一个二维数组 requirements 表示。这个二维数组的每个元素是一个长度为 3 的一维数组，对于某个剧情的触发条件 c[i], r[i], h[i]，如果当前 C >= c[i] 且 R >= r[i] 且 H >= h[i] ，则剧情会被触发。

# 根据所给信息，请计算每个剧情的触发时间，并以一个数组返回。如果某个剧情不会被触发，则该剧情对应的触发时间为 -1 。

# 示例 1：

# 输入： increase = [[2,8,4],[2,5,0],[10,9,8]] requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]

# 输出: [2,-1,3,-1]

# 解释：

# 初始时，C = 0，R = 0，H = 0

# 第 1 天，C = 2，R = 8，H = 4

# 第 2 天，C = 4，R = 13，H = 4，此时触发剧情 0

# 第 3 天，C = 14，R = 22，H = 12，此时触发剧情 2

# 剧情 1 和 3 无法触发。

# 示例 2：

# 输入： increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]] requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]

# 输出: [-1,4,3,3,3]

# 示例 3：

# 输入： increase = [[1,1,1]] requirements = [[0,0,0]]

# 输出: [0]

# 限制：

# 1 <= increase.length <= 10000
# 1 <= requirements.length <= 100000
# 0 <= increase[i] <= 10
# 0 <= requirements[i] <= 100000

# 
# 思路1 二分查找， 1136 ms 40.38%
# 注意二分查找的本质是猜测值，每次筛选一半的数据。
# 时间复杂度 n + lgn 其实就是O(n) 

# 思路2 使用map存储 384 ms 97.92%
# 查找的时间复杂度是O(1),总体时间复杂度依然是O(n)
# 这个查找速度极快。 辅助空间大小稍大，使用了全部的resource sum作为key

from typing import List
class Solution:
    #  思路1 二分查找， 1136 ms 40.38%
    # def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
    #     s = [[0,0,0]]
    #     for a,b,c in increase:
    #         _a,_b,_c = s[-1]
    #         s.append([a+_a, b+_b, c+_c])

    #     size = len(s)

    #     ans = []
    #     maxa, maxb, maxc = s[-1]

    #     for a,b,c in requirements:
    #         if a > maxa or b > maxb or c> maxc:
    #             ans.append(-1)
    #             continue
    #         elif a == 0 and b == 0 and c == 0:
    #             ans.append(0)
    #             continue

    #         low, high = 0, size-1

    #         while low <= high:
    #             mid = (low+high) // 2
    #             if mid == 0 :
    #                 ans.append(-1)
    #                 break
                    
    #             _a,_b,_c = s[mid]
    #             _a1, _b1, _c1 = s[mid - 1]
    #             if (_a >= a and _b >= b and _c >= c ) and (_a1 < a or _b1 < b or _c1 < c):
    #                 ans.append(mid)
    #                 break

    #             elif _a >= a and _b >= b and _c >= c :
    #                 high = mid - 1
    #             else :
    #                 low = mid + 1
        
    #     return ans

    # 思路2 使用map 384 ms 97.92%
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        resource_c, resource_r, resource_h = {0:0}, {0:0}, {0:0}
        sum_c, sum_r, sum_h = 0, 0, 0
        day = 0 
        for c, r, h in increase:            
            day += 1

            for i in range(1, c + 1) : resource_c[sum_c + i] = day
            for i in range(1, r + 1) : resource_r[sum_r + i] = day
            for i in range(1, h + 1) : resource_h[sum_h + i] = day

            sum_c += c
            sum_r += r
            sum_h += h

        # print(resource_c, resource_r, resource_h)

        n = len(requirements)
        ans = [-1 for _ in range(n)]

        for i in range(n):
            _c, _r, _h = requirements[i]
            day_c = resource_c.get(_c, -1)
            day_r = resource_r.get(_r, -1)
            day_h = resource_h.get(_h, -1)

            if day_c > -1 and day_r > -1 and day_h > -1 :
                ans[i] = max(day_c, day_h, day_r)

        return ans

            

            
# print(Solution().getTriggerTime( [[5,1,0],[1,0,7]], [[6,12,3],[4,5,8]]))
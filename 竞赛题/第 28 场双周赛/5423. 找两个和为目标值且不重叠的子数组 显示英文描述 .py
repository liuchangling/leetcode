# 5423. 找两个和为目标值且不重叠的子数组 显示英文描述 
# 题目难度Medium
# 给你一个整数数组 arr 和一个整数值 target 。

# 请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。

# 请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。

 

# 示例 1：

# 输入：arr = [3,2,2,4,3], target = 3
# 输出：2
# 解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
# 示例 2：

# 输入：arr = [7,3,4,7], target = 7
# 输出：2
# 解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
# 示例 3：

# 输入：arr = [4,3,2,6,2,3,4], target = 6
# 输出：-1
# 解释：我们只有一个和为 6 的子数组。
# 示例 4：

# 输入：arr = [5,5,4,4,5], target = 3
# 输出：-1
# 解释：我们无法找到和为 3 的子数组。
# 示例 5：

# 输入：arr = [3,1,1,1,5,1,2,1], target = 3
# 输出：3
# 解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
 

# 提示：

# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 1000
# 1 <= target <= 10^8

# 这道题真不敢信是一个medium
# 用到了前缀和和dp。
# 滑动窗口的代码我看了一下实现极为丑陋，故不做实现

# 我们可以依次遍历，了解到有哪些i...j 满足子序列和为target？
from collections import defaultdict
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        presum = {0:-1}  # map, key是前缀和,value是其结尾下标. 这里加了一个下标-1的0
        tmp = 0 # 一个临时变量用于计算前缀和
        dp = [] # dp[i] 0~i中， 满足和为target的子数组长度最小值，一个子数组 或者是1e8(表示0个子数组)
        ans = 1e8 # 记录答案
        pre_shortest = 1e8 # 用于记录之前遇到最短的和为target的子数组长度，是dp思路的空间优化，只使用一个值保存

        for idx, value in enumerate(arr):
            tmp += value
            presum[tmp] = idx # 计算前缀和

            if tmp - target in presum:
                # m + target = tmp 代表有一段以idx结尾的子数组之和为target
                i = presum[tmp-target] # 即 arr[0...i] + target = arr[0...idx], i+1就是这次子数组的起点
                cur_length = idx - i # 以idx结尾的和为target子数组的长度

                pre_shortest = min(pre_shortest, cur_length)
                dp.append(pre_shortest)

                if i!= -1 and dp[i] < 1e8: # 0~i 存在一个满足条件的子数组，则更新ans
                    ans = min(ans, cur_length + dp[i])

            else:
                # 如果没有这样的子数组则设为pre_shortest,开始是1e8，一旦成功过一次，则会更新为前置最小值。
                dp.append(pre_shortest)

        return ans if ans < 1e8 else -1 # 这里别忘了处理-1


        

print(Solution().minSumOfLengths([3,2,2,4,3], 3))
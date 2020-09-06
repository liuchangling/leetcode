# 删除最短的子数组使剩余数组有序 

# 题目难度Medium
# 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

# 一个子数组指的是原数组中连续的一个子序列。

# 请你返回满足题目要求的最短子数组的长度。

 

# 示例 1：

# 输入：arr = [1,2,3,10,4,2,3,5]
# 输出：3
# 解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
# 另一个正确的解为删除子数组 [3,10,4] 。
# 示例 2：

# 输入：arr = [5,4,3,2,1]
# 输出：4
# 解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
# 示例 3：

# 输入：arr = [1,2,3]
# 输出：0
# 解释：数组已经是非递减的了，我们不需要删除任何元素。
# 示例 4：

# 输入：arr = [1]
# 输出：0
 

# 提示：

# 1 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^9

# dp[i] 为 以i结尾，保持有序， 需要删除的个数
# 显然dp[0] = 0
# dp[i] = dp[j] + i-1-j 其中j满足 arr[i]>=arr[j] 然后删除j+1 ~ i-1之间的东西
# 另外保存剩余最大长度和需要删除的最小值
# 就是硬贪，先找到右侧最长升序子序列的开始位置，然后从左侧开始遍历。 左侧数字可插入到右侧子序列的位置 和 左侧数字当前所在位置 之间的数字可被删除，
# 确认一下最少删除的数字数量即可。查找插入的过程，可以用二分查找进行优化，如果用 Python，可以直接使用 bisect 库即可。


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
       import bisect
        # 右侧最长升序子序列
        right_begin = 0
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                right_begin = i
                break

        # 删除左侧所有数字的长度
        result = right_begin
        if result == 0:
            return 0

        # 左侧最长上升子序列
        for i in range(0, len(arr)):
            if i > 0 and arr[i] < arr[i - 1]:
                break
            # 二分查找当前数字在右侧可插入的位置，当前数字的下标和插入位置之间的数字可被删除
            index = bisect.bisect_left(arr, arr[i], right_begin)
            result = min(result, index - 1 - i)
            # print(arr[i], index, result)
        return result
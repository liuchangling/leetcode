# 5419. 两个子序列的最大点积
# 题目难度Hard
# 给你两个数组 nums1 和 nums2 。

# 请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。

# 数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。


# 示例 1：

# 输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# 输出：18
# 解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
# 它们的点积为 (2*3 + (-2)*(-6)) = 18 。
# 示例 2：

# 输入：nums1 = [3,-2], nums2 = [2,-6,7]
# 输出：21
# 解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
# 它们的点积为 (3*7) = 21 。
# 示例 3：

# 输入：nums1 = [-1,-1], nums2 = [1,1]
# 输出：-1
# 解释：从 nums1 中得到子序列 [-1] ，从 nums2 中得到子序列 [1] 。
# 它们的点积为 -1 。
 

# 提示：

# 1 <= nums1.length, nums2.length <= 500
# -1000 <= nums1[i], nums2[i] <= 100

# 点积：

# 定义 a = [a1, a2,…, an] 和 b = [b1, b2,…, bn] 的点积为：
# a'b = a1b1+a2b2+...anbn

# 思路肯定是dp
# 对于dp的定义可以分为以ij为结尾和截止目前为止两种。思路区别不大
# 以ij为结尾的思路需要额外的一个ans作为变量进行比较


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1) + 1
        l2 = len(nums2) + 1

        # dp 定义为一个左上角为0作为base
        # dp[i+1][j+1]定义为nums1[0~i]  nums2[0~j]的最大值
        # 所以dp数组长度为l2+1, l1+1, 注意这个for循环先创建的是一维的行
        dp = [[-200000 for j in range(l2)] for i in range(l1)] 
        dp[0][0] = 0
       
        # 计算dp二维矩阵的值
        for i in range(1, l1):
            for j in range(1, l2): 
                # print(nums1[i-1], nums2[j-1])

                # 这个状态转移方程比较复杂，细品
                dp[i][j] = max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1],  
                               nums1[i - 1] * nums2[j - 1],
                               dp[i][j - 1], 
                               dp[i-1][j]) 
        
        
        return dp[-1][-1]
#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#
# https://leetcode-cn.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (47.69%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    15.9K
# Total Submissions: 30.3K
# Testcase Example:  '[8,1,5,2,6]'
#
# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
# 
# 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
# 
# 返回一对观光景点能取得的最高分。
# 
# 
# 
# 示例：
# 
# 输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
# 
# 
# 思路1 快慢指针87%
#       一次遍历，记录左侧最大的A[i]+i, 更新ans和idx即可
# 
# 思路2  发现idx其实没有用， 另外测试案例的len不用控制。实际上速度居然下降了 73%

# @lc code=start
class Solution:
    # def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # L = len(A)
        # if L < 2 : return 0

        # ans = A[0] + A[1] - 1
        # idx = 0 if A[0] - 0 > A[1] - 1 else 1
        # lastValue = A[idx] + idx

        # for i in range(2,L):
        #     ans = max (lastValue + A[i] - i, ans)
        #     if A[i] + i  > lastValue: 
        #         idx = i
        #         lastValue = A[i] + i

        # return ans
    
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre_max = A[0]
        ans = 0
        for i in range(1,len(A)):
            ans = max(ans, pre_max+A[i]-i)
            pre_max = max(pre_max, A[i]+i)
        
        return ans
# @lc code=end


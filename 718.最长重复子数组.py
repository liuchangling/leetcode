#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (49.95%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    31.8K
# Total Submissions: 60.1K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 
# 
# 示例：
# 
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 思路1 一维dp
# dp[i] 代表 B[0~i]和A的最长重复子数组长度
# dp[i+1] = max(用了B[i+1] , dp[i])
# 那么只需要考虑以B[i+1]结尾的最长重复子数组长度即可
# 
# 写的时候发现考虑以B[i+1]结尾的问题又可以进一步dp


# 思路2 二维dp 5924ms 24%
# 我们已经发现了这个题逆序遍历比较方便
# dp[i][j]代表 A[i:]和B[j:]的公共最长前缀, 需使用A[i]B[j]开头
# A[i] == B[j]时 dp[i+1][j+1] = dp[i][j] +1 
# A[i] != B[j]时 dp[i+1][j+1] = 0


# 思路3 优化后的滑动窗口 

# @lc code=start
class Solution:

    # 思路2 二维dp 5924ms 24%
    # def findLength(self, A: List[int], B: List[int]) -> int:
    #     lena, lenb = len(A), len(B)
    #     dp = [[0] * (lenb + 1) for _ in range(lena + 1)]
    #     ans = 0

    #     for i in range(lena-1, -1, -1):
    #         for j in range(lenb-1, -1, -1):
    #             dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
    #             ans = max(ans, dp[i][j])

    #     return ans


    # 思路3 优化后的滑动窗口 368ms
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)

        if m>n:
            m, n, A, B = n, m, B, A

        tmp_list = []
        result = 0

        str_B = ',' + ','.join([str(i) for i in B]) + ','

        for r in A:
            tmp_list.append(str(r))

            # 如果加入最右元素，字符串依然在B里面，就更新result
            if ',' + ','.join(tmp_list) + ',' in str_B:
                result = max(result, len(tmp_list))

            else:
                # 否则将最早插入的tmp_list移除
                # 有趣的是，这时候其实长度是不会变的。因为更短的长度即使在B中，也没有意义，面向答案编程
                tmp_list = tmp_list[1:]

        return result


        
        
        
# @lc code=end


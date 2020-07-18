#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Hard (40.14%)
# Likes:    270
# Dislikes: 0
# Total Accepted:    25.7K
# Total Submissions: 59K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
# 
# 示例 1:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false

# 思路dp 56ms 40% 
# dp[i][j] s1的0~i-1 和s2的0~j-1 能否组成s3的 0~i+j-1
# dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1]== s3[i+j-1])


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False


        I,J = len(s1)+1, len(s2)+1
        dp = [[False for j in range(J)] for i in range(I)]
        dp[0][0] = True

        for j in range(1,J):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1,I):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for i in range(1, I):
            for j in range(1, J):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1]== s3[i+j-1])
        
        # print(dp)

        return dp[-1][-1]
# @lc code=end


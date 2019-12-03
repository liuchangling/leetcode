#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
# 暴力法思考： 对每个startindex，遍历endIndex。检查子串是否回文，并更新最大值
# 算法时间复杂度为 O(n^3) 因为判断是否为回文也需要一个o(n)复杂度
# 方法1: 对于某一个midIndex +-length 找到左右最长边界，并最终更新最大值
# 算法时间复杂度为 O(n^2) 感觉已经很不错咧？ 
# 排名时间80+% 内存 99+%
# -------
# 看了一波答案。。。我直接写出了官方方法4，自豪一波
# 然后官方推荐了Manacher算法，但是没有给出具体实现。我去google一下
# 额令人震惊的是，Manacher是一个O(n)算法。。。
# https://www.jianshu.com/p/116aa58b7d81
# 这里提到了一个我们之前做题目4，为了解决奇偶问题，加虚拟#的方式，很秀
# 具体时间之后处理吧



# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ''
        maxLen = 0
        maxStr = s[0]
        for i in range(length):
            if i - maxLen // 2 < 0 or i + maxLen//2 >= length:
                continue
            t = 0
            for j in range(1, i + 1):
                if i+j >= length:
                    break
                if s[i - j] == s[i + j]:
                    t += 1
                else:
                    break

            q = 0
            for k in range(i+1):
                if i+k+1 >= length:
                    break
                if s[i-k] == s[i+k+1]:
                    q += 1
                else:
                    break
            
            temp = max(2 * t + 1, 2 * q)

            if temp > maxLen:
                maxLen = temp
                if 2 * t + 1 > 2 * q:
                    maxStr = s[i-t: i+t+1]
                else:
                    maxStr = s[i-q+1: i+q+1]

        return maxStr


print(Solution().longestPalindrome('aaa'))
# @lc code=end

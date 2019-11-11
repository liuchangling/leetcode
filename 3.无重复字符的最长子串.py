#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# 一次遍历，如果遇到重复或者结束就更新max
# 遇到重复时，删掉temp[0:index+1] 其中index为上一个重复字符的下标
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        temp = []
        for b in s :
            if b in temp:
                if len(temp) > max:
                    max = len(temp)
                del temp[0 : temp.index(b)+1]
                temp.append(b)
            else:
                temp.append(b)
        if len(temp) > max:
            max = len(temp)

        # print(max)
        return max


Solution().lengthOfLongestSubstring('pwwkew')
# @lc code=end


#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# 一次遍历，如果遇到重复或者结束就更新max
# 遇到重复时，删掉temp[0:index+1] 其中index为上一个重复字符的下标

# 更好的思路是滑动窗口
# 每次移动有指针，如果新字符在窗口中已经出现过，就更新max
# 并将左指针移动到上一次出现这个字符的右侧
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = []
        for b in s :
            if b in temp:
                ans = max(ans, len(temp))
                del temp[0 : temp.index(b)+1]
                temp.append(b)
            else:
                temp.append(b)
                
        ans = max(ans, len(temp))

        # print(max)
        return ans


Solution().lengthOfLongestSubstring('pwwkew')
# @lc code=end


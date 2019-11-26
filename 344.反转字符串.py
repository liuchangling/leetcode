#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t = len(s)
        l = t >> 1
        
        for i in range(l):
            s[i], s[t - i - 1] = s[t - i - 1], s[i]


Solution().reverseString(["h", "e", "l", "l", "o"])

# @lc code=end

#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
# 这道题比较简单
# 当n 能被4整除的时候 ，先手拿k 后手采取拿4-k的策略，能保证后手必胜。即返回False
# 当n 不能被4整除时， 先手拿 n % 4 。 后手面对的问题类似先手在能被4整除的石头中取。
# 即此情况先手必胜

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        
# @lc code=end


#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#
# https://leetcode-cn.com/problems/divisor-game/description/
#
# algorithms
# Easy (67.83%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    48.2K
# Total Submissions: 67.4K
# Testcase Example:  '2'
#
# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
# 
# 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
# 
# 
# 选出任一 x，满足 0 < x < N 且 N % x == 0 。
# 用 N - x 替换黑板上的数字 N 。
# 
# 
# 如果玩家无法执行这些操作，就会输掉游戏。
# 
# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：2
# 输出：true
# 解释：爱丽丝选择 1，鲍勃无法进行操作。
# 
# 
# 示例 2：
# 
# 输入：3
# 输出：false
# 解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 1000
# 思路1 模拟dp 106ms
# dp[0] = false
# dp[1] = false
# dp[2] = true
# dp[3] = false
# 对于dp[4]， 1，2都可以当x dp[4] = !dp[3] or !dp[2] = true
# 即先手拿1 后手相当于先手的dp[3] 所以先手赢 dp[4] = true
# 对于dp[5] , x只能等于1 那么dp[5] = !dp[4] = false
# 倒退就知道了
# dp[i] = (!dp[i - x])
# 思路2 数学法 44ms
# 官方数学法，奇数必败，偶数必胜
# 然后用数学归纳法证明了一下。。。怕了怕了

from functools import lru_cache

# @lc code=start
class Solution:
    # 106ms    
    # @lru_cache(None)
    # def divisorGame(self, N: int) -> bool:
    #     for i in range(1,N):
    #         if N % i == 0 :
    #             if not self.divisorGame(N - i):
    #                 return True

    #     return False

    #44ms
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0 
        
# @lc code=end

 
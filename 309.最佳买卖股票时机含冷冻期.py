#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (53.29%)
# Likes:    465
# Dislikes: 0
# Total Accepted:    46.5K
# Total Submissions: 82K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
# 思路dp 97%
# 这个蛮有意思的, 是个二维dp 不过第二维是一个常量, 最大值为数量,本来还以为要写3个dp数组出来，就是没想到搞个二维

# 我们用 f[i] 表示第 i 天结束之后的「累计最大收益」。根据题目描述，由于我们最多只能同时买入（持有）一支股票，并且卖出股票后有冷冻期的限制，因此我们会有三种不同的状态：

# 我们目前持有一支股票，对应的「累计最大收益」记为 f[i][0]；

# 我们目前不持有任何股票，并且处于冷冻期中，对应的「累计最大收益」记为 f[i][1]；

# 我们目前不持有任何股票，并且不处于冷冻期中，对应的「累计最大收益」记为 f[i][2]。

# 状态转移方程直接看：这里懒得描述了，实现是自己写的  97%
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-4/


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices : return 0 

        size = len(prices)
        dp = [[0] * 3 for _ in range(size)]
        dp[0][0] = -prices[0]

        ans = 0 
        
        for i in range(1, size):
            dp[i][0] = max(dp[i-1][0] , dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

            ans = max(ans, dp[i][0], dp[i][1], dp[i][2])

        return ans



        
# @lc code=end


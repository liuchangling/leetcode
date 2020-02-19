#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (56.06%)
# Likes:    592
# Dislikes: 0
# Total Accepted:    117.5K
# Total Submissions: 204.4K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 
# 
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 思路1 顺序遍历，
# 如果上涨就不管，除非遇到了尾
# 如果跌了或者持平，就更新一下sum和lastMin 这种算法时间在5%。。。
#
# 思路2 更简单了 如果上涨了就连续相加，注意可以视为第二天卖了又买回来
#      其实和1的时间复杂度一样，但代码简洁清晰了很多。不过也是在5%。。。
#      不知道是不是服务器变慢了。 居然比同样代码的js运行慢3倍

# @lc code=start
class Solution:
    # 思路1
    # def maxProfit(self, prices: List[int]) -> int:

    #     if prices == []:
    #         return 0

    #     length = len(prices)
    #     lastMin = prices[0]
    #     sum = 0

    #     for i in range(1,length):
    #         # 涨
    #         if prices[i] > prices[i-1] :
    #             if i == length - 1 and prices[i] > lastMin:
    #                 sum = sum + prices[i] - lastMin
    #         else :
    #             # 跌或持平
    #             if prices[i-1] > lastMin:
    #                 sum = sum + prices[i-1] - lastMin
    #             lastMin = prices[i]
        
    #     return sum

    # 思路2
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                s = s + prices[i] - prices[i-1]
        return s

# @lc code=end


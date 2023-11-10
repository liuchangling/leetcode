#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.25%)
# Likes:    739
# Dislikes: 0
# Total Accepted:    127.7K
# Total Submissions: 243.9K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 
# 注意你不能在买入股票前卖出股票。
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 思路1  从左到右计算最小值数组；从右到左计算最大值数组，两数组对应位置相减得出一个max值返回 
# 思路2  用两个变量分别存储峰谷和当前最大值 官方解法超越5%。。感觉今天服务器很渣诶
#

# @lc code=start
class Solution:
    # 思路2
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0

        sum = 0
        low = prices[0]

        for i in range(1, length):
            if prices[i] > prices[i-1]:
                sum = max( sum, prices[i] - low)
            if prices[i] < low:
                low = prices[i]
        
        return sum

# @lc code=end


# js
# /**
#  * @param {number[]} prices
#  * @return {number}
#  */
# var maxProfit = function(prices) {
#     let min = prices[0]
#     let ret = 0

#     for(let i = 1; i<prices.length; i++){
#         if(prices[i] > min){
#             ret = Math.max(prices[i] - min, ret)
#         }else{
#             min = prices[i]
#         }
#     }

#     return ret

# };
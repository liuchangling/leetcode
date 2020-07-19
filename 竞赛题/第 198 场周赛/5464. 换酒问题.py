# 小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

# 如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

# 请你计算 最多 能喝到多少瓶酒。


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0 
        left = 0 
        while numBottles > 0 :
            # print(numBottles)
            
            ans += numBottles

            numBottles, left = (numBottles + left)  // numExchange,   (numBottles + left) % numExchange
            

        return ans



print(Solution().numWaterBottles(9, 3))
print(Solution().numWaterBottles(15, 4))
print(Solution().numWaterBottles(5, 5))
print(Solution().numWaterBottles(2, 3))
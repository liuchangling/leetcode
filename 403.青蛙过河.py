#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#
# https://leetcode-cn.com/problems/frog-jump/description/
#
# algorithms
# Hard (32.33%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 17.4K
# Testcase Example:  '[0,1,3,4,5,7,9,10,12]'
#
# 一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。
# 
# 给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时，
# 青蛙默认已站在第一个石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。
# 
# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。
# 
# 请注意：
# 
# 
# 石子的数量 ≥ 2 且 < 1100；
# 每一个石子的位置序号都是一个非负整数，且其 < 2^31；
# 第一个石子的位置永远是0。
# 
# 
# 示例 1:
# 
# 
# [0,1,3,5,6,8,12,17]
# 
# 总共有8个石子。
# 第一个石子处于序号为0的单元格的位置, 第二个石子处于序号为1的单元格的位置,
# 第三个石子在序号为3的单元格的位置， 以此定义整个数组...
# 最后一个石子处于序号为17的单元格的位置。
# 
# 返回 true。即青蛙可以成功过河，按照如下方案跳跃： 
# 跳1个单位到第2块石子, 然后跳2个单位到第3块石子, 接着 
# 跳2个单位到第4块石子, 然后跳3个单位到第6块石子, 
# 跳4个单位到第7块石子, 最后，跳5个单位到第8个石子（即最后一块石子）。
# 
# 
# 示例 2:
# 
# 
# [0,1,2,3,4,8,9,11]
# 
# 返回 false。青蛙没有办法过河。 
# 这是因为第5和第6个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
# 
# 思路1 通过从开始往后遍历，推算每个能落脚的位置下一个能到哪，
# 数据结构为当前位置对应通过上一次跳跃多少步到

# 思路2 针对思路1代码太丑 稍微美化了一点
# 思路3 先定义了key，对于不落在该key的直接丢弃，有一定提升。 速度73%空间100%。。。

# @lc code=start
class Solution:
    # def canCross(self, stones: List[int]) -> bool:
    #     can = {0 : {0}} # 表示到达第n个位置可能通过哪几种步数到达，这里的value是一个set，用于去重。

    #     for s in stones:
    #         if s in can:
    #             k = can[s]
    #             for e in k:
    #                 # 这段代码比较重复，总体做的就是更新can。 
    #                 # 由于for in不支持长度变更，所以对于0和1不要做add操作，否则会抛异常
    #                 if e-1 + s in can:
    #                     if e > 1:
    #                         can[e-1 + s].add(e-1)
    #                 else :
    #                     can[e-1+s] = {e-1}

    #                 if e+s in can:
    #                     if e > 0 :
    #                         can[e + s].add(e)
    #                 else:
    #                     can[e+s] = {e}

    #                 if e+1+s in can :
    #                     can[e+1 + s].add(e+1)
    #                 else:
    #                     can[e+1+s] = {e+1}

    #     # print(can)
    #     return stones[-1] in can

    # def canCross(self, stones: List[int]) -> bool:
    #     can = {0:{0}}

    #     for s in stones:
    #         if s in can:
    #             steps = can[s]
    #             for k in steps:
    #                 for i in [k-1, k, k+1]:
    #                     if i > 0:
    #                         if s + i in can:
    #                             can[s+i].add(i)
    #                         else:
    #                             can[s+i] = {i}
            
    #     return stones[-1] in can

    def canCross(self, stones: List[int]) -> bool:
        can = {}
        for stone in stones:
            can[stone] = set()
        can[0] = {0}
        
        for stone in stones:
            # print(can, stone)
            for k in can[stone]:
                for i in [k-1, k, k+1]:
                    if i > 0 and i + stone in can:
                        can[i + stone].add(i)
        
        return len(can[stones[-1]]) > 0
# @lc code=end


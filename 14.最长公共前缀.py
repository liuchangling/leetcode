#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
# 我的思考：
# 方案1 用一个临时变量，比如指向列表的第一个值
#      每次和后一个字符串比较，提取公共前缀部分。 速度排名在81%左右
# ----- 
# 以上在官方题解被称为水平扫描法。。。
# 对了答案：
# 官方提出上面算法的一个问题，就是如果最后一个字符串是最短的，这种扫描方法会费时间，
# 于是提出了
# 方案2 每次比较全部字符串的一列
#      一顿操作猛如虎 实际上速度差不多还是80%。。。
# 方法3 分治法，开始用空间换时间了。比较花了。
#      前一半的公共最长前缀和后一半的公共最长的计算结果就是公共最长
#      不想实现，实际上这种情况如果其中一个已经得到了“”，另一边也要算半天，有些场景不合适
#      而且需要额外空间处理，没啥兴趣写
# 方法4 二分查找法 速度超过了99.53%！最优解
#      对于方法2的改进，需要提前知道整个数组的最小长度 作为L。然后就是二分查找0-L中那个是对的
#      小的半边符合要求，那么向右搜，扩大范围，左边不再比较
#      小的半边不符合要求，那么向左搜，缩小范围，右边不再比较
# 方法5  元组拆包set法 only for python
#       有个大佬用了个最短代码实现 最优雅
#       思路是将strs视为二维char的矩阵，合并之后，一个个组合对应项，如果对应项放在集合里面长度
#       为1，则继续往后看一位，否则返回。代码精简到令人咋舌。时间性能高达惊人的97%。。。

# @lc code=start
from typing import List
class Solution:
    # 方案1 自己想的 排名80%
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) <= 0 :
    #         return ""

    #     prefix = strs[0]
    #     for s in strs :
    #         if prefix == "":
    #             return prefix

    #         t = ""
    #         l = len(prefix)
            
    #         for index, c in enumerate(s):
    #             if index >= l:
    #                 break
    #             elif c == prefix[index] :
    #                 t = t + c
    #             else :
    #                 break

    #         prefix = t

    #     return prefix

    # 方案2走起 排名80% 官方版会修改原数组，个人不是很喜欢
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) == 0 or strs[0] == "":
    #         return ""
    #     a = 0 
    #     length = len(strs[0])

    #     needSearch = True
    #     while(needSearch):
    #         if a == length:
    #             break
    #         c = strs[0][a] # 取第一个字符串的字符
    #         for s in strs:
    #             if len(s) == a or s[a] != c:
    #                 #位数不够了 或者不是公共字符了
    #                 needSearch = False
    #                 return strs[0][0:a]
    #         a += 1
            
    #     return strs[0][0:a]

    # 官方方案1  排名80% 看似短了一点，实际上算法核心和速度差不多
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) == 0:
    #         return ""
    #     prefix = strs[0]

    #     for index,s in enumerate(strs):
    #         if len(strs) > index > 0:
    #             while s.find(prefix) != 0 :
    #                 prefix = prefix[0: len(prefix) - 1]
    #                 if prefix is None or prefix == "":
    #                     return ""
        
    #     return prefix

    # 对方法3无爱，跳过。直接看最优解4和最优雅解 5

    # 方法4:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""
        minLen = len(strs[0])
        for s in strs:
            minLen = min(len(s), minLen)
        
        low = 0
        height = minLen

        while low <= height:
            mid = (low + height) // 2
            if self.isCommonPrefix(strs, low, height):
                # 左边都ok哦,丢弃左边,向右搜索
                low = mid + 1
            else :
                # 左边不ok
                height = mid - 1
        return strs[0][0:low - 1]

    def isCommonPrefix(self, strs: List[str], l:int, h:int)->bool:
        m = (l + h ) // 2
        pre = strs[0][0:m]
        for element in strs:
            if not pre == element[0:m]:
                return False

        return True
 

    # 方法5 某大佬最短代码实现
    # def longestCommonPrefix(self, strs: List[str]) -> str:     
    #     s = ""
    #     for i in zip(*strs):
    #         if len(set(i)) == 1:
    #             s += i[0]
    #         else:
    #             break
    #     return s


# js version
# var longestCommonPrefix = function(strs) {
#     let minLen = Math.min(...strs.map(i=>i.length))
#     let zip = new Array(minLen)
#     const s = strs[0]

#     strs.forEach(str=>{
#         for(let i = 0; i<minLen; i++){
#             if(!zip[i]){
#                 zip[i] = new Set()
#             }
#             zip[i].add(str[i])
#         }
#     })

#     let ret = ''
#     for(let i = 0; i<minLen; i++){
#         if(zip[i].size === 1){
#             ret += s[i]
#         }else{
#             return ret
#         }
#     }
#     return ret

# };


#print(Solution().longestCommonPrefix(["flower","flow","flight"]))

# @lc code=end
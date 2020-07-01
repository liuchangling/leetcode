#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (37.94%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 45.6K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 
# 说明：
# 
# 
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# 示例 2：
# 
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
# 
# 
#
from typing import List
from functools import lru_cache

# @lc code=start
class Solution:

    # 思路1  dfs代码简洁，但是aaaaabaaaa的测试用例会超时。。。
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    #     dic = set(wordDict)
    #     size = len(s)
    #     ans = []

    #     @lru_cache(None) 因为list不可以lrucache，所以这里用上了元祖，实际上会超出lrucache的范围。。
    #     def dfs(idx: int, path)-> bool:
    #         # print(idx)
    #         if idx >= size : 
    #             ans.append(path)
    #             return True

    #         for i in range(idx+1, size+1):
    #             word = s[idx:i]
    #             if word in dic:                     
    #                 tmp = path + (word,)
    #                 dfs(i, tmp)
            
    #         return False


        
    #     dfs(0, ())

    #     ret = [' '.join(i) for i in ans]
    #     # print(ret)

    #     return ret


    # 思路1 dfs优化 加入对于dict的长度判断 44ms 89%
    # def wordBreak(self, s: str, wordDict: list) -> list:
    #     if not s:
    #         return []
    #     _len, wordDict = len(s), set(wordDict)  # 转换成字典用于O(1)判断in
    #     _min, _max = 2147483647, -2147483648   # 记录字典中的单词的最长和最短长度，用于剪枝
    #     for word in wordDict:
    #         _min = min(_min, len(word))
    #         _max = max(_max, len(word))

    #     def dfs(start):  # 返回s[start:]能由字典构成的所有句子
    #         if start not in memo:
    #             res = []
    #             for i in range(_min, min(_max, _len-start)+1):  # 剪枝，只考虑从最小长度到最大长度查找字典
    #                 print(s[start: start+i])
    #                 if s[start: start+i] in wordDict:  # 找到了
    #                     res.extend(list(map(lambda x: s[start: start+i]+' '+x, dfs(start+i))))  # 添加
    #             memo[start] = res  # 加入记忆
    #         return memo[start]

    #     memo = {_len: ['']}  # 初始化记忆化存储
    #     return list(map(lambda x: x[:-1], dfs(0)))  # 去掉末尾多出的一个空格



    # 思路2 dp 没错dp[j]太大，直接内存溢出了。。 实际上很多解法是先判断是否有解，有解再执行。。。
    # 所以加了一先判断是否有解的代码。。。  40ms 95%

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not self.check(s, wordDict): return []

        size = len(s)
        dp = [[] for i in range(size + 1) ]
        dp[0] = ['']

        dic = set(wordDict)

        _min, _max = 2147483647, -2147483648
        for word in wordDict:
            _min = min(_min, len(word))
            _max = max(_max, len(word))

        for i in range(size):
            if dp[i]:
                for j in range(i+_min, min(i+_max, size)+1):
                    word = s[i:j]
                    if word in dic: 
                        dp[j] = dp[j] + [ s+ ' ' +word for s in dp[i]]
            
        return [s[1:] for s in dp[-1]] # 去除第一个空格


    def check(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False for i in range(size + 1) ]
        dp[0] = True        

        dic = set(wordDict)

        for i in range(size):
            if dp[i]:
                for j in range(i+1, size+1):
                    if s[i:j] in dic: dp[j] = True
            
        return dp[-1]

# @lc code=end

# print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))


# print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
# print(Solution().wordBreak("aaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
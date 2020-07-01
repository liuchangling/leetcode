#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (44.66%)
# Likes:    559
# Dislikes: 0
# Total Accepted:    73.3K
# Total Submissions: 157.7K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
# 思路1 dp  52ms
# dp[i]代表 s[0~i-1]能否拆分成字典值
# 比较特殊，不在后面依靠前面的推，
# 而是通过dp[i]为true时，我们直接把后续能为true的标记起来
# 
# 思路1的优化，我们将visited标记带上 时间差不多

# 思路2 双层循环dp遍历 48ms O(n2)

# 思路3 回溯+记忆 48ms
#      找到一个在dict中的词后，未使用部分继续调用backtrack 
#      这里的回溯就是i+=1

# 思路4 dfs版本 44ms

from functools import lru_cache

# @lc code=start
class Solution:
    # # 思路1  52ms
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     size = len(s)
    #     dp = [False for i in range(size + 1) ]
    #     dp[0] = True        

    #     dic = set(wordDict)

    #     flag = 0 # s[0~flag-1] 可以拆分的意思

    #     while flag < size :
    #         idx = -1
    #         # 找flag+1 ~ size-1
    #         for i in range(flag+1,size+1):
    #             if not dp[i]:
    #                 if s[flag:i] in dic: #s[flag~i]在字典中，那么0~i可以拆分
                        
    #                     dp[i] = True

    #                     if idx < 0 : idx = i
    #             else :
    #                 if idx < 0: idx = i
            

    #         if idx > 0 : 
    #             flag = idx
    #         else:
    #             break

    #     return dp[-1]
    
    # 思路2  52ms 没啥变化
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # size = len(s)
        # dp = [False for i in range(size + 1) ]
        # dp[0] = True
        # visited = [False for i in range(size + 1)]
        # visited[0] = True

        # dic = set(wordDict)

        # flag = 0 # s[0~flag-1] 可以拆分的意思

        # while flag < size :
        #     idx = -1
        #     # 找flag+1 ~ size-1
        #     if not visited[flag + 1]:
        #         visited[flag+1] = True
        #         for i in range(flag+1,size+1):
        #             if not dp[i]:
        #                 if s[flag:i] in dic: #s[flag~i]在字典中，那么0~i可以拆分
                            
        #                     dp[i] = True

        #                     if idx < 0 : idx = i
        #             else :
        #                 if idx < 0: idx = i
        #     else :
        #         for i in range(flag+1, size+1):
        #             if dp[i]:
        #                 idx = i
        #                 break
                        
            

        #     if idx > 0 : 
        #         flag = idx
        #     else:
        #         break

        # return dp[-1]


        # 思路2 直接双层循环遍历 48ms
        # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #     size = len(s)
        #     dp = [False for i in range(size + 1) ]
        #     dp[0] = True        

        #     dic = set(wordDict)

        #     for i in range(size):
        #         if dp[i]:
        #             for j in range(i+1, size+1):
        #                 if s[i:j] in dic: dp[j] = True
                
        #     return dp[-1]
    
        # 思路3 回溯 48ms
        # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #     dic = set(wordDict)

        #     @lru_cache(None) #记忆化函数 避免重复计算。
        #     def backtrack(s):
        #         if not s : return True #表示已经使用中的单词已分割完。

        #         # print(s)

        #         res = False
        #         for i in range(len(s) + 1) :
        #             if s[:i] in dic:
        #                 #若 s[0,⋯,i−1] 在 wordDict 中 ,是否能被拆分就看s[i....]是否也能拆分
        #                 res = res or backtrack(s[i:])
                 
        #         return res

        #     return backtrack(s)


        # 思路4 dfs 44ms
        def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            dic = set(wordDict)
            size = len(s)

            @lru_cache(None)
            def dfs(idx: int)->bool:
                if idx >= size : return True

                for i in range(idx+1, size+1):
                    if s[idx:i] in dic and dfs(i):
                        return True
                
                return False

            return dfs(0)


        # 思路5 bfs 52ms 这个没有办法通过lrucache记忆化，所以通过visited进行优化
        # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #     dic = set(wordDict)
        #     size = len(s)
        #     visited = [False for _ in range(size+1)]

        #     queue = [0] 
        #     while queue:
        #         start = queue.pop(0)
        #         if visited[start]: continue                

        #         visited[start] = True

        #         for end in range(start+1, size + 1):
        #             if s[start:end] in dic :
        #                 if end == size: return True #end指针已经越界，即所有节点遍历完了

        #                 queue.append(end) #单词存在于单词表，且end未到头，将end推入队列作为下一层节点


        #     return False
                    

# "ab"\n["a","b"]
# "leetcode"\n["leet","code"]
# @lc code=end


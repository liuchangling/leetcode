#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (41.70%)
# Likes:    325
# Dislikes: 0
# Total Accepted:    42.1K
# Total Submissions: 100K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#  思路1  BFS遍历，  TLE了。。。  32/43 pass 比较是否只差一位执行了太多次

#  思路2  优化：用了一个通配符的hash表 时间O(MN) 空间O(MN)
# 广搜时我们需要访问 Dug 的所有邻接点，我们可以先生成 Dug 的所有通用状态：
# Dug => *ug
# Dug => D*g
# Dug => Du*


# 思路3  双向BFS， 即同时从beginWord和endWord进行搜索，如果同时指向相同通配符就可以返回
#        虽然复杂度依然是时间O(MN) 空间O(MN) 但这样做时间和空间都可以减半


# @lc code=start

from typing import List
from collections import defaultdict


class Solution:
    # 思路1 BFS   TLE...
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     m = { 1 : [beginWord]}
    #     level = 1

    #     size = len(wordList)

    #     visited = [False for _ in range(size)]

    #     founded = True


    #     def diff(a,b):
    #         diffCount = 0 
    #         for i in range(len(a)):
    #             if a[i] != b[i]:
    #                 diffCount += 1
            
    #         return diffCount == 1

    #     while founded:
    #         founded = False
    #         m[level + 1] = []
    #         for i in range(size):               
    #             if not visited[i]:
    #                 for lastLevel in m[level]:
    #                     word = wordList[i]
    #                     print(word)
    #                     if diff(lastLevel, word) == 1:
    #                         if word == endWord:
    #                             return level + 1


    #                         m[level + 1].append(word)
                          
    #                         visited[i] = True
    #                         founded = True
      
    #         level += 1
    #     return 0 

    # # 思路2 51%
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

    #     if endWord not in wordList or not endWord or not beginWord or not wordList:
    #         return 0

    #     dictory = defaultdict(list)
    #     L = len(beginWord)

    #     # 准备过程  将字典中其中一位用*代替，建立map    
    #     for word in wordList:
    #         for i in range(L):
    #             dictory[word[:i] + '*' + word[i+1:]].append(word)
                
    #     visited = set()
    #     visited.add(beginWord)

    #     queue = [(beginWord, 1)]

    #     while queue:
    #         current_word , level = queue.pop(0)

    #         for i in range(L):
    #             tmp = current_word[:i] + "*" + current_word[i+1:]
    #             for word in dictory[tmp]:
    #                 if word == endWord:
    #                     return level + 1

    #                 if word not in visited:
    #                     visited.add(word)
    #                     queue.append((word, level+1))

    #             # 遍历过一次之后，这个通配符就可以删掉了，避免以后重复判断，这个清空非常nice
    #             dictory[tmp] = []
        
    #     return 0

    # 思路3 90% 双端bfs
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        dictory = defaultdict(list)
        L = len(beginWord)

        # 准备过程  将字典中其中一位用*代替，建立map    
        for word in wordList:
            for i in range(L):
                dictory[word[:i] + '*' + word[i+1:]].append(word)
                
        queue_begin = [(beginWord, 1)]        
        queue_end = [(endWord, 1)]

        # 这次我们不仅要知道有米有访问过，还需要知道距离起点有多少距离。所以用了个map，而非set
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}


        def visitWordNode(q, v1, v2): # v1 当前遍历的已访问数组， v2另一端已访问的数组
            current_word, level = q.pop(0)            

            for i in range(L):
                tmp = current_word[:i] + "*" + current_word[i+1:]

                for word in dictory[tmp]:
                    # 如果能相遇，直接返回两个level之和
                    if word in v2:
                        return level + v2[word]
                    if word not in v1:
                        # 这段逻辑是没有变的
                        v1[word] = level + 1
                        q.append((word, level + 1))
            return None

        while queue_begin and queue_end:
            # 从头向后一次
            ans = visitWordNode(queue_begin, visited_begin, visited_end)
            if ans : return ans

            # 从尾向前一次
            ans = visitWordNode(queue_end, visited_end, visited_begin)
            if ans: return ans


        return 0

# print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

        
# @lc code=end


#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode-cn.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (31.56%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    11.7K
# Total Submissions: 34.6K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord
# 的最短转换序列。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: []
# 
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
# 
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        dictory = defaultdict(list)
        L = len(beginWord)

        # 准备过程  将字典中其中一位用*代替，建立map    
        for word in wordList:
            for i in range(L):
                dictory[word[:i] + '*' + word[i+1:]].append(word)
                
        queue_begin = [(beginWord, [[beginWord]])]        
        queue_end = [(endWord, [[endWord]])]

        # 这次value定义为到目前节点位置所有可能的路径，是个二维矩阵
        visited_begin = {beginWord: [[beginWord]]}
        visited_end = {endWord: [[endWord]]}

        ans = [] # 记录路径

        def visitWordNode(q, v1, v2, dir): # v1 当前遍历的已访问数组， v2另一端已访问的数组
            current_word, paths = q.pop(0)            

            for i in range(L):
                tmp = current_word[:i] + "*" + current_word[i+1:]

                for word in dictory[tmp]:
                    # 如果能相遇，直接添加path
                    if word in v2:
                        for p1 in paths:
                            for p2 in v2[word]:
                                if dir:
                                    ans.append(p1 + p2)
                                else :
                                    ans.append(p2 + p1)

                                print(ans, word, q)
                    if word not in v1:
                        # 这段逻辑是没有变的
                        t = []
                        for p in paths:
                            if dir:
                                t.append(p+[word])
                            else:
                                t.append([word]+p)
                        v1[word] = t
                        q.append((word, t))
            return None

        while len(ans) == 0:
            # 从头向后一次
            visitWordNode(queue_begin, visited_begin, visited_end, True)

            # 从尾向前一次
            visitWordNode(queue_end, visited_end, visited_begin, False)

        return ans
# @lc code=end


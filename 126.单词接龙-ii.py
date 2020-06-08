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
# 127题的升级版
# 思路1  单向bfs 时间超越5% 空间超越50%。。。
# 思路2  双向bfs。。。 我不知道咋写终止条件，官方题解这次也没啥追求，写的很一般。。
#        看了个答案 时间超越100% 空间超越50% 仔细研究一下。。。
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    # 思路1 自己写的单向bfs 5%。。坑爹
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     if endWord not in wordList or not endWord or not beginWord or not wordList:
    #         return []

    #     dictory = defaultdict(list)
    #     L = len(beginWord)

    #     # 准备过程  将字典中其中一位用*代替，建立map    
    #     for word in wordList:
    #         for i in range(L):
    #             dictory[word[:i] + '*' + word[i+1:]].append(word)
                
    #     ans = []

    #     queue_begin = [(beginWord, 1, [[beginWord]])]
    #     visited_begin = {beginWord:[[beginWord]]}

    #     minLevel = len(wordList) + 1 # 最大长度为字典长度+1

    #     while queue_begin:
    #         current_word,level, paths = queue_begin.pop(0)

    #         if level > minLevel: continue            

    #         for i in range(L):
    #             tmp = current_word[:i] + '*' + current_word[i+1:]
    #             for word in dictory[tmp]:
    #                 if word == endWord:
    #                     # 拼接路径
    #                     for p in paths:
    #                         minLevel = level
    #                         ans.append(p + [endWord])
                            
    #                 elif word not in visited_begin:
    #                     new_paths = [p+[word] for p in paths]
    #                     visited_begin[current_word] = new_paths
    #                     queue_begin.append((word, level+1, new_paths))

    #     return ans


    # 思路2 抄来的双向bfs
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        # 定义了从头向后访问的集合，从尾向前访问的集合
        # 将wordlist转成了set，方便做减法运算。定义了默认首次访问方向为向后
        forward, backward, wordList, flag = {beginWord}, {endWord}, set(wordList), True  
        # 所有字符，用于取代通配符，词长度， dic的key和value都是单词，value表示parent，或者说前置节点的意思。这里前置和后置的关系取决于距离beginword和endWord的距离
        # dic 或者说 指向的是离beginWord距离更近一层的节点。一种BFS的思想。
        letters, length, dic = 'abcdefghijklmnopqrstuvwxyz', len(beginWord), defaultdict(set)
        while forward:
            if len(forward) > len(backward): # 当向后方向的长度大于向前方向长度时，反转以下三个值。 处理了困扰我n久的双向遍历时最大深度问题。。。
                forward, backward, flag = backward, forward, not flag

            wordList -= forward  # 从wordList移除将要遍历的forward ， 这样顺便将wordList当做了visited用，很棒的想法
            cur = set()
            for word in forward:
                # 这个循环我们将未插入dic的节点中，层数+1的节点全部插入dic。注意两个方向有区别。
                for i in range(length):
                    left, right = word[:i], word[i+1:]  #老生常谈的通配符
                    for l in letters:  # l类似我们之前用的通配符*
                        w = left + l + right  # 这个用letters处理，免去了构造一整个dict的过程，节约了很多代码和额外空间
                        if w in wordList:
                            cur.add(w)
                            if flag:
                                dic[w].add(word)    # 单词w可由word变化而来， 这里 w 比 word 离 beginWord远
                            else:
                                dic[word].add(w)    # 这个意思是逆序遍历时， 视为word可由w变化而来。这里 w 比word 离 endWord远，就是说离beginWord更近
            
            #很酷炫的写法，利用了集合的交集 &计算出的是一个set。
            if cur & backward:  # 产生交集，最短路径找到  
                # 用于生成全部路径，开始只放一个尾结点，通过dic不停找前置节点获取全路径
                # 这是一个二维数组， 第一维表示全部的路径，第二维表示该路径下的全部节点。
                res = [[endWord]] 
                while res[0][0] != beginWord:  # 循环结束条件是刚添加进去的节点是beginWord
                    # 这也是体现算法功底的代码。 遍历的是全部的路径， i代表的是其中一条路径，
                    # i[0]代表的是每个路径的最前置节点，即第一个点。 注意我们每次都会清空之前的res，进行重新赋值。
                    # 去除第一个点之后，通过dic[i[0]]获取前置节点x， 拼接路径：[x]+i
                    # 这个代码干了这么多事，两层循环，但简洁优雅，又透露出算法功底，很佩服原作者！
                    res = [[x]+i for i in res for x in dic[i[0]]]
                return res  # 产生交集就return,避免了我写的那个有5层又有6层的情况。很妙
            # 这个有一种指针向后移动的意味， 其实代表的是该层遍历结束，我们向后/向前移动一层。 类似常写的 cur = cur.next
            forward = cur
        return []
# @lc code=end

# print(Solution().findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
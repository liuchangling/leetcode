# 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

# 注意：本题相对原题稍作改动，只需返回未识别的字符数

#  

# 示例：

# 输入：
# dictionary = ["looked","just","like","her","brother"]
# sentence = "jesslookedjustliketimherbrother"
# 输出： 7
# 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
# 提示：

# 0 <= len(sentence) <= 1000
# dictionary中总字符数不超过 150000。
# 你可以认为dictionary和sentence中只包含小写字母。


# 思路1 自己写的  dp 1632 ms 14%
# dp[i+1] 定义为sentence到i为止的未匹配字符数
# dp[0] = 0
# dp[1] = 0 if sentence[0] in dictionary else 1 .... 
# 假设 dicitionary 中单词最大长度为n
# dp[k] 意味着sentence[0:k]未匹配的字符数， 检测sentence[k:i]是否在dictionary里面
# 状态转义方程  dp[i] = min( dp[i-1]+ check(s[i-1:i]),dp[i-2]+check(s[i-2:i])  ...  )
# 

# 思路2 dp优化 1100ms 26%
# 直觉想法中有过多的比较次数
# 我们可以直接使用dictionary的词去匹配sentence,即判断
# for word in dictionary : if sentence[i-len(word):i]  == word

# 思路3  dp极限优化版用了记忆dfs的思想 68ms 99%
# 大佬就是大佬，看完我裂开了
# 先抹去了不存在的字典中的词，然后通过lrucache的递归将效率提高的很高
# 先计算了所有word可能的长度k，直接dp[i] = min[dp[i+k]+check(sentence(i:i+k))]
# 同时还用了dp的内存优化。酷炫的不行 i了i了
# 注意这次其实是逆序从尾到头进行dp的或者可以说类似dfs

# 思路4  对于查询字符串是否在字典中有个很棒的数据结构，叫字典树
#    常用于搜索。也叫前缀树。和hash相比的好处是，用户输入的时候，输入前几个字符也能找到对应的匹配可能性，
#    而hash必须全部输入完，才能进行match
#    字典树的实现在"前缀树.py"中

from typing import List

class Solution:
    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     dictionary = set(dictionary)
    #     n = 0
    #     for word in dictionary:
    #         n = max(n, len(word))
        
    #     size = len(sentence) + 1

    #     dp = list(range(size))

    #     def check(s):
    #         return 0 if s in dictionary else len(s)


    #     for i in range(1, size):
    #         k = 0 
    #         while k <= i and k <= n:
    #             dp[i] = min(dp[i], dp[i-k] + check(sentence[i-k:i]) )
    #             k += 1
    #     # print(dp)
    #     return dp[-1]


    # dp优化，状态转移方程的优化 
    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     dictionary = set(dictionary)

    #     size = len(sentence) + 1

    #     dp = [0] * size

    #     for i in range(1, size):
    #         dp[i] = dp[i-1] + 1 
    #         for word in dictionary:
    #             k = len(word)
    #             if i >= k :
    #                 t = dp[i-k] if sentence[i-k:i] == word else dp[i-k]+k
    #                 dp[i] = min(dp[i], t)

    #     return dp[-1]

    # 思路3  大佬dp 68ms 99%
    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     dictionary = set([w for w in dictionary if sentence.find(w)!=-1])
    #     lens = list({len(w) for w in dictionary})
    #     lens.sort(reverse = True)
    #     N, res, i = len(sentence), 0, 0
    #     @functools.lru_cache(maxsize=1000)
    #     def sol(i) : # 递归
    #         if i >= N : return 0
    #         tails = []
    #         tails = [sol(i+l) for l in lens if i+l <= N and sentence[i:i+l] in dictionary]
    #         tails += [1+sol(i+1)]
    #         return (min(tails) if tails else 0)

    #     return sol(0)

    # 思路4 字典树 5384 ms 7.6%
    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     root = Trie()
    #     root.insert_all(dictionary)

    #     size = len(sentence) + 1
    #     dp = [0] * size

    #     n = 0
    #     for word in dictionary:
    #         n = max(n, len(word))

    #     for i in range(1, size):
    #         dp[i] = dp[i-1] + 1 
            
    #         for j in range(i-1, max(-1, i-n-1), -1):
    #             # 这种写法依然有重复比较
    #             if root.search(sentence[j:i]):
    #                 dp[i] = min(dp[i],dp[j])
    #             # 这里可以加入字典中单词最大值最小值，加速跳过                    
                
        
    #     return dp[-1]

    # 思路5 字典树 564 ms 70.97%
    def respace(self, dictionary: List[str], sentence: str) -> int:
        root = Trie()
        root.insert_all(dictionary)

        size = len(sentence) + 1
        dp = [0] * size

        for i in range(1, size):
            dp[i] = dp[i-1] + 1 
            
            pointer = root
            # 这里其实是改版的search 插入了dp更新的代码
            for j in range(i, -1, -1):
                ch = sentence[j-1]
                c = ord(ch) - ord('a')
                if pointer.isEnd:
                    dp[i] = min(dp[i], dp[j])
                
                if c not in pointer.children:
                    break
                pointer = pointer.children[c]
        
        return dp[-1]

    



class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word:str):
        # 这里逆序插入
        p = self
        for ch in word[::-1]:
            c = ord(ch) - ord('a')
            print(c)
            if c not in p.children :
                p.children[c] = Trie()
            p = p.children[c]

        p.isEnd = True

    def insert_all(self, words:List[str]):
        for word in words:
            self.insert(word)

    def search(self, word:str):
        s = word[::-1] # 逆序查找
        p = self
        for ch in s:
            c = ord(ch) - ord('a')
            if c not in p.children:
                return False
            p = p.children[c]

        return p.isEnd



# print(Solution().respace(["looked","just","like","her","brother"] , "jesslookedjustliketimherbrother"))
Solution().respace(["a"] , "aa")
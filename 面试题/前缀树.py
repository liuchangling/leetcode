
from typing import List

# 标准前缀树
class Trie:
    def __init__(self):
        self.children = {} # 我们直接使用一个dict模拟TreeNode,而非list
        # 用于标记是否为一个完整单词，因为可能有abc ab两个单词，这时候bc的isEnd应该为True
        # 该属性在search中用到
        self.isEnd = False 

    # 将单词插入到字典中。实际调用中应该都往一个空的起点插入
    def insert(self, word: str):
        p = self # 类似链表从第一个元素开始遍历
        for ch in word: # 类似链表的新增。逐渐将一个个子母添加到后面
            if ch not in p.children:
                p.children[ch] = Trie() # 如果是首次遇到这个字母，就建立一个新的节点
            p = p.children[ch] # 类似 node = node.next() 将p后移到儿子辈
        p.isEnd = True # 最后一个字母的p是一个完整单词
    
    def insert_all(self, words:List[int]): # 一起插入
        for word in words:
            self.insert(word)

    def search(self, word:str): # 用于查询单词是否在字典中
        p = self
        for ch in word:
            # 特殊情况，如果是字符a-z 可以用ch - 'a', 这样只需要存储一个0~25的数字
            if ch not in p.children: # 一个一个字符匹配
                return False # 匹配失败则返回
            else:
                p = p.children[ch] #否则继续比较下一位

        return p.isEnd # 比较完之后返回是否是完整单词，避免单词是abc，查询a返回true

    # 和search类似，现在只需要比较单词是否是字典中的某个前缀
    # 类似用户输入appl 的时候 猜测用户想输入apple。而非全部search
    def startWith(self, pre:str): 
        p = self
        for ch in pre:
            if ch not in p.children:
                return False
            else: 
                p = p.children[ch]
        
        return True




root = Trie()

root.insert_all(['abc', 'bcd','a'])
print(root)

print(root.search('ab'))
print(root.startWith('ab'))



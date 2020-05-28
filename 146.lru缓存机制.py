#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (45.95%)
# Likes:    594
# Dislikes: 0
# Total Accepted:    59.7K
# Total Submissions: 123.3K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
# 
# 
# 
# 进阶:
# 
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 
# 
# 示例:
# 
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
# 
# 
# 一个双向链表，加一个散列完成 击败53%
# 原生python有  collections.OrderedDict 可以击败99%。 不过这个就没有达到训练目的了
# 类似的java有LinkedHashMap
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.dic = collections.OrderedDict()
#         self.remain = capacity

#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         v = self.dic.pop(key) 
#         self.dic[key] = v   # set key as the newest one
#         return v      

#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:    
#             self.dic.pop(key)
#         else:
#             if self.remain > 0:
#                 self.remain -= 1  
#             else:  # self.dic is full
#                 self.dic.popitem(last=False) 
#         self.dic[key] = value

# @lc code=start
class DLinkedNode:
    def __init__(self, key =0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
      self.capacity = capacity
      self.cache = {} 
      self.count = 0 
      # 从尾部插入，从头部弹出
      self.head = DLinkedNode()
      self.tail = DLinkedNode()

      self.head.next = self.tail
      self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self.moveToEnd(n)
            return n.value
        else :
            return -1 


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            n = self.cache[key]
            n.value = value
            self.moveToEnd(n)
        else :
            n = DLinkedNode(key, value)            
            self.appendToEnd(n)
            self.count += 1
            self.cache[key] = n
            if self.count > self.capacity:
                self.pop()
                self.count -= 1

    def moveToEnd(self, n:DLinkedNode) -> None:
        # 把n前后先连上
        n.prev.next = n.next
        n.next.prev = n.prev
        # 把n移动到尾部
        self.appendToEnd(n)
        

    def appendToEnd(self, n:DLinkedNode) -> None:
        n.next = self.tail
        n.prev = self.tail.prev

        self.tail.prev.next = n
        self.tail.prev = n

    def pop(self) -> None:
        self.cache.pop(self.head.next.key)
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


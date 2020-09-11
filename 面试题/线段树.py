# 定义的每个节点为

class Node:
    # 起点到终点的聚合值
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = None

class SegementTree:
    def __init__(self, nums):
        self.data = nums
        self.size = len(nums)
        self.tree = [None] * len(nums) * 4
        
        # 0空着，因为 2*0 2*0+1不能表示0的左右儿子，
        # 所以我们把1作为根
        self.rootIndex = 1

        self.buildTree(self.rootIndex, 0, len(nums) - 1)     
    
    def mergeFn(self,a,b): #聚合方法为sum
        return a+b

    
    def buildTree(self, i, start, end):
        self.tree[i] = Node(start, end)

        if start == end : # 递归终止条件为区间长度=1
            self.tree[i].value = self.data[start]
            return

        mid = (start + end) // 2 
        self.buildTree(2*i, start, mid) # 构建左子树
        self.buildTree(2*i+1, mid+1, end) # 构建右子树

        # 构建完成后聚合左右子树的数据
        self.tree[i].value = self.mergeFn(self.tree[2*i].value , self.tree[2*i + 1].value)


    def update(self, i, value):
        self.setValue(self.rootIndex, i, value) #从根开始找目标位置设置值


    def setValue(self, currentIdx, targetIdx, value):
        cur = self.tree[currentIdx]
        if cur.start == cur.end: #已经到了叶子节点
            cur.value = value
            return

        mid = (cur.start + cur.end)/2

        # 递归找到targetIdx 并更新 
        if currentIdx <= mid:
            self.setValue(2 * currentIdx, targetIdx, value)
        else :
            self.setValue(2 * currentIdx + 1, targetIdx, value)

        # 然后修正父节点的值
        self.tree[currentIdx].value = self.mergeFn(self.tree[currentIdx * 2].value, self.tree[currentIdx * 2+1].value)

    # 查询left到right之间的统计值
    def query(self, currentIdx, left, right):
        cur = self.tree[currentIdx]
        if cur.start == left and cur.end == right:
            return cur.value
        
        mid = (cur.start + cur.end) // 2
        if right <= mid:
            # left...right区间均在mid左侧，那么就到cur的左子树中找
            return self.query(2*currentIdx, left, right)
        elif left >= mid + 1:
            # left...rigth区间均在mid右侧，那么就到cur的右子树中找
            return self.query(2*currentIdx+1, left, right)
        else:
            # left <= mid <= right
            return self.mergeFn( self.query(2*currentIdx, left, mid), self.query(2*currentIdx+1, mid+1 , right) )

    def get(self, i, j):
        return self.query(self.rootIndex, i, j)



seg = SegementTree([1,3,5])
print(seg.get(0,1))
print(seg.get(1,2))
print(seg.get(0,2))

seg.update(1,2)

print(seg.get(0,1))
print(seg.get(1,2))
print(seg.get(0,2))



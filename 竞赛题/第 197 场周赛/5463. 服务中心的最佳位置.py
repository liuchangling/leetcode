# 一家快递公司希望在新城市建立新的服务中心。公司统计了该城市所有客户在二维地图上的坐标，并希望能够以此为依据为新的服务中心选址：使服务中心 到所有客户的欧几里得距离的总和最小 。

# 给你一个数组 positions ，其中 positions[i] = [xi, yi] 表示第 i 个客户在二维地图上的位置，返回到所有客户的 欧几里得距离的最小总和 。

# 换句话说，请你为服务中心选址，该位置的坐标 [xcentre, ycentre] 需要使下面的公式取到最小值：

# sqrt((xcentre - xi)^2 - (ycentre - yi)^2)
# 与真实值误差在 10^-5 之内的答案将被视作正确答案。

# 示例 1：



# 输入：positions = [[0,1],[1,0],[1,2],[2,1]]
# 输出：4.00000
# 解释：如图所示，你可以选 [xcentre, ycentre] = [1, 1] 作为新中心的位置，这样一来到每个客户的距离就都是 1，所有距离之和为 4 ，这也是可以找到的最小值。
# 示例 2：



# 输入：positions = [[1,1],[3,3]]
# 输出：2.82843
# 解释：欧几里得距离可能的最小总和为 sqrt(2) + sqrt(2) = 2.82843
# 示例 3：

# 输入：positions = [[1,1]]
# 输出：0.00000
# 示例 4：

# 输入：positions = [[1,1],[0,0],[2,0]]
# 输出：2.73205
# 解释：乍一看，你可能会将中心定在 [1, 0] 并期待能够得到最小总和，但是如果选址在 [1, 0] 距离总和为 3
# 如果将位置选在 [1.0, 0.5773502711] ，距离总和将会变为 2.73205
# 当心精度问题！
# 示例 5：

# 输入：positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
# 输出：32.94036
# 解释：你可以用 [4.3460852395, 4.9813795505] 作为新中心的位置
 

# 提示：

# 1 <= positions.length <= 50
# positions[i].length == 2
# 0 <= positions[i][0], positions[i][1] <= 100

# 这个的基础知识我欠缺了，做不了

# 三分查找介绍
# 类似于二分查找，三分搜索法也是比较常用的基于分治思想的高效查找方法。但是和二分不同，二分只适用于单调函数，比如常用的对单调递增或单调递减的一个序列中的某一个元素进行查找，三分却突破了这种限制，可以用于左边递增右边递减或者相反的，这么一类函数，也就是常说的凸函数和凹函数。但是为什么三分法可以用于凸函数或者凹函数呐，这其实是因为这种函数总是有一个最大值或者最小值，这样就可以借此判断出三分法中两个中点相对相对于极值的位置，例如下图（凹函数类似）：
# 三分搜索的实现主要是判断midl和midr所在值的大小。以凸函数为例（凹函数类似，只是判mid大小的时候保留小的即可（其实也是保留离极值最近的mid）），先以left和right为端点计算出它们的中点midl，然后再以midl和right为端点计算出它们的中点midr，接下来就需要判断f(midl)和f(midr)值的大小了，如果f(midl)大于f(midr)，那么说明midl靠近极值，此时令right=midr，否则说明midr靠近极值，此时则令left=midl，总之就是要保留离极值最近的那一个mid，然后重复前面的过程，直到left和right十分接近，最终f(left)就等于了极值，下面给出程序实现：



class Solution:
    # scipy api 736 ms
    # from scipy.optimize import minimize
    # def getMinDistSum(self, positions: List[List[int]]) -> float:
    #     def getSum(x):
    #         return sum([sqrt((x[0] - x1) ** 2 + (x[1] - y1) ** 2) for x1, y1 in positions])
    #     return minimize(getSum, [50, 50]).fun

    # # 三分查找 5740 ms

    # def getMinDistSum(self, positions: List[List[int]]) -> float:
    #     # 到各点距离之和
    #     def dis(x, y):
    #         return sum([((px - x) ** 2 + (py - y) ** 2) ** 0.5 for px, py in positions])

    #     # 三分找最小
    #     def three_divide(l, r, f, k=50):
    #         for i in range(k):
    #             m = l + (r - l) / 3
    #             mm = r - (r - l) / 3
    #             if f(m) < f(mm):
    #                 r = mm
    #             else:
    #                 l = m
    #         return (l + r) / 2

    #     # 左右边界
    #     lmin, rmax = 0, 100

    #     # 外层查x的值函数
    #     def xf(mx):
    #         # 内层查y的值函数
    #         def yf(my): return dis(mx, my)
    #         return dis(mx, three_divide(lmin, rmax, yf))

    #     x = three_divide(lmin, rmax, xf)
    #     y = three_divide(lmin, rmax, lambda my: dis(x, my))
    #     return dis(x, y)

    # 手写梯度下降 108ms
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        LEN = len(positions)
        x0,y0 = sum(positions[i][0] for i in range(LEN))/LEN, sum(positions[i][1]/LEN for i in range(LEN)) # 合适的初始值，坐标的算数平均值
        
        def f(x0,y0): # 求距离
            return sum(((x-x0)**2+(y-y0)**2)**0.5 for x,y in positions)

        def df(x0,y0): # 求距离的梯度
            dx=dy=0
            for x,y in positions:
                vx,vy = x-x0,y-y0
                r = (vx*vx+vy*vy)**0.5
                if r==0:
                    continue
                dx+=vx/r
                dy+=vy/r
            return dx,dy
        step = 16
        while((g:=df(x0,y0))!=(0.0,0.0)):
            dx,dy = g
            x1,y1 = x0+dx*step,y0+dy*step
            while(f(x1,y1)>=f(x0,y0)):
                if (dx**2+dy**2)*step<10**(-5):
                    return f(x0,y0)
                step/=4
                x1,y1 = x0+dx*step,y0+dy*step
            x0,y0 = x1,y1
       
        return f(x0,y0)

/*
 * @lc app=leetcode.cn id=307 lang=javascript
 *
 * [307] 区域和检索 - 数组可修改
 *
 * https://leetcode-cn.com/problems/range-sum-query-mutable/description/
 *
 * algorithms
 * Medium (56.50%)
 * Likes:    166
 * Dislikes: 0
 * Total Accepted:    13.7K
 * Total Submissions: 24.1K
 * Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
 *
 * 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
 * 
 * update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
 * 
 * 示例:
 * 
 * Given nums = [1, 3, 5]
 * 
 * sumRange(0, 2) -> 9
 * update(1, 2)
 * sumRange(0, 2) -> 8
 * 
 * 
 * 说明:
 * 
 * 
 * 数组仅可以在 update 函数下进行修改。
 * 你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。
 * 
 * 
 */

// 比较直接的想法是保存前缀和，o(n)修改 O(1)merge 这里实现了一下
// 如果要求O(1)修改 o(n)merge就用普通array就行

// 然而这道题说明了 update和merge频次差不多， 实际上最适合的结构是线段树
// 线段树可以在lgn的时间完成update和merge

// 线段树的每个节点都包含数组一段范围[i:j]的聚合信息，min/max/sum等
// 左右节点分别包含[i:(i+j)//2] ，[(i+j)//2 + 1: j]的信息
// 线段树可以用数组或者树实现、对于数组实现，节点i的左节点为2i 右节点为2i+1

// 线段树的标准步骤为：
// 1. 从给定数组构建线段树的预处理步骤。
// 2. 修改元素时更新线段树。
// 3. 使用线段树进行区域和检索。


// @lc code=start
// /**
// 前缀和 216ms
//  * @param {number[]} nums
//  */
// var NumArray = function(nums) {
//     this.data = nums
//     this.preSum = [] //  加到当前位置的前缀和
//     let count = 0 
//     nums.forEach(i =>{
//         count += i
//         this.preSum.push(count)        
//     })
// };

// /** 
//  * @param {number} i 
//  * @param {number} val
//  * @return {void}
//  */
// NumArray.prototype.update = function(i, val) {
//     let diff = val - this.data[i] 
//     this.data[i] = val
//     for(let j = i; j < this.data.length; j ++){
//         this.preSum[j] += diff
//     }
// };

// /** 
//  * @param {number} i 
//  * @param {number} j
//  * @return {number}
//  */
// NumArray.prototype.sumRange = function(i, j) {
//     if(i == 0 ) return this.preSum[j];

//     return this.preSum[j] - this.preSum[i-1]
// };


// // 线段树 168 ms	
// /**
//  * @param {number[]} nums
//  */
var NumArray = function(nums) {
    this.n = nums.length
    // buildTree
    // 我们0~n-1 存储父节点的信息，先空着。
    let data = new Array(this.n)
    
    // 叶节点存在n ~ 2n-1的位置。
    data = data.concat(nums)
    for(let i = this.n-1; i > 0; i--){
        // 然后计算每个父节点的值。就是所谓的范围内的聚合信息
        data[i] = data[2*i] + data[2*i+1]        
    }
    
    this.data = data;
};


/** 
 * @param {number} i 
 * @param {number} val
 * @return {void}
 */
NumArray.prototype.update = function(i, val) {
    // 修改i 其实变动的是data[n + i] = val
    // 然后对于 i//2 进行更新
    this.data[this.n+i] = val
    let j = (this.n+i) >> 1
    while(j > 0){
        this.data[j] = this.data[2*j] + this.data[2*j+1]
        j >>= 1
    }
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    let left = this.n + i;
    let right = this.n + j;
    let sum = 0;

    while(left <= right){
        // 注意因为left == right时不可能 &1 既是1又是0，所以就在这个循环顺便解决了
        // 本来在考虑是否要把 left == right拎出来单独计算的
        if (left % 2 == 1){
            // 是父亲的右儿子，那么求和时需要丢弃左儿子           
            sum += this.data[left];
            // 并直接将left指向父节点的右兄弟
            left++;
        }

        if(right % 2 == 0){
            // 为父亲的左儿子，那么求和时需要丢弃右儿子
            sum += this.data[right];
            // 并直接将right指向父节点的左兄弟
            right--;
        }

        // 如果前面未修改，则直接向上一层
        left >>= 1
        right >>= 1 

    }

    return sum;

};



/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(i,val)
 * var param_2 = obj.sumRange(i,j)
 */
// @lc code=end


var obj = new NumArray([1,3,5])
var param_2 = obj.sumRange(0,2)



// class SegmentTree {

//     constructor(arr,handler) {
//       this.handler = handler;
//       this.items = arr.map(item => item);
//       this.tree = new Array(this.items.length * 4);
//       if (arr.length) {
//           this.buildSegmentTree(0, 0, this.items.length - 1);
//       }
//     }
  
//     getSize() {
//       return this.items.length;
//     }
  
//     isEmpty() {
//       return this.getSize() === 0;
//     }
  
//     get(index) {
//       if (index >= 0 && index < this.items.length) {
//         return this.items[index];
//       }
  
//       return undefined;
//     }
  
//     query(leftIndex, rightIndex){
//       // 校验区间的合法性
//       if (leftIndex < 0 || leftIndex >= this.items.length || rightIndex < 0 || rightIndex >= this.items.length || leftIndex > rightIndex) {
//         return undefined;
//       }
  
//       return this.querySegment(0, 0, this.items.length - 1, leftIndex, rightIndex);
//     }
  
//     set(index, el) {
//       if (index < 0 || index >= this.items.length) {
//         return false;
//       }
  
//       this.setValue(0, 0, this.items.length - 1, index, el);
//       return true;
//     }
  
//    setValue(rootIndex, leftIndex, rightIndex, index, el) {
//       if (leftIndex === rightIndex) {
//         this.tree[rootIndex] = el;
//         return;
//       }
  
//       const leftChild = this.getLeftChildIndex(rootIndex);
//       const rightChild = this.getRightChildIndex(rootIndex);
//       const middle = leftIndex + Math.floor((rightIndex - leftIndex) / 2);
  
//       if (index > middle) {
//         this.setValue(rightChild, middle + 1, rightIndex, index, el);
//       } else {
//         this.setValue(leftChild, leftIndex, middle, index, el);
//       }
  
//       this.tree[rootIndex] = this.handler(this.tree[leftChild], this.tree[rightChild]);
//     }
  
//     // 在以rootIndex为根的线段树中[leftIndex,...,rightIndex]的范围里，搜索区间[queryLeftIndex,...,queryRightIndex]的值
//    querySegment(rootIndex, leftIndex, rightIndex, queryLeftIndex, queryRightIndex) {
//       if (leftIndex === queryLeftIndex && rightIndex === queryRightIndex) {
//         return this.tree[rootIndex];
//       }
  
//       const leftChild = this.getLeftChildIndex(rootIndex);
//       const rightChild = this.getRightChildIndex(rootIndex);
//       const middle = leftIndex + Math.floor((rightIndex - leftIndex) / 2);
  
//       // 查询区间的左边界在右半部分，整体在整个树的右边
//       if (queryLeftIndex > middle) {
//         return this.querySegment(rightChild, middle + 1, rightIndex, queryLeftIndex, queryRightIndex);
//       }
  
//       // 查询区间右边界在左半部分，整体在整个树的左边
//       if (queryRightIndex <= middle) {
//         return this.querySegment(leftChild, leftIndex, middle, queryLeftIndex, queryRightIndex);
//       }
  
//       // 左边界在左半部分，右边界在右半部分
//       const leftResult = this.querySegment(leftChild, leftIndex, middle, queryLeftIndex, middle);
//       const rightResult = this.querySegment(rightChild, middle + 1, rightIndex, middle + 1, queryRightIndex);
//       return this.handler(leftResult, rightResult);
//     }
  
//     // 在rootIndex的位置创建表示区间[leftIndex,...,rightIndex]的线段树
//      buildSegmentTree(rootIndex, leftIndex, rightIndex) {
//       if (leftIndex === rightIndex) {
//         this.tree[rootIndex] = this.items[leftIndex];
//         return;
//       }
  
//       const leftChild = this.getLeftChildIndex(rootIndex);
//       const rightChild = this.getRightChildIndex(rootIndex);
//       const middle = leftIndex + Math.floor((rightIndex - leftIndex) / 2);
  
//       // 将leftIndex-rightIndex区间再分成2半进行构造
//       this.buildSegmentTree(leftChild, leftIndex, middle);
//       this.buildSegmentTree(rightChild, middle + 1, rightIndex);
  
//       // 最后根节点的值等于左右两个节点处理过的值
//       this.tree[rootIndex] = this.handler(this.tree[leftChild], this.tree[rightChild]);
//     }
  
//      getLeftChildIndex(index) {
//       return 2 * index + 1;
//     }
  
//     getRightChildIndex(index) {
//       return 2 * index + 2;
//     }
//   }
  
//   /**
//    * @param {number[]} nums
//    */
//   var NumArray = function(nums) {
//       this.tree = new SegmentTree(nums, (a, b) => a + b)
//   };
  
//   /** 
//    * @param {number} i 
//    * @param {number} val
//    * @return {void}
//    */
//   NumArray.prototype.update = function(i, val) {
//       return this.tree.set(i, val)
//   };
  
//   /** 
//    * @param {number} i 
//    * @param {number} j
//    * @return {number}
//    */
//   NumArray.prototype.sumRange = function(i, j) {
//       return this.tree.query(i, j)
//   };
  
//   /**
//    * Your NumArray object will be instantiated and called as such:
//    * var obj = new NumArray(nums)
//    * obj.update(i,val)
//    * var param_2 = obj.sumRange(i,j)
//    */
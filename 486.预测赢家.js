/*
 * @lc app=leetcode.cn id=486 lang=javascript
 *
 * [486] 预测赢家
 *
 * https://leetcode-cn.com/problems/predict-the-winner/description/
 *
 * algorithms
 * Medium (52.68%)
 * Likes:    294
 * Dislikes: 0
 * Total Accepted:    25K
 * Total Submissions: 43.6K
 * Testcase Example:  '[1,5,2]'
 *
 * 给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，……
 * 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
 * 
 * 给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：[1, 5, 2]
 * 输出：False
 * 解释：一开始，玩家1可以从1和2中进行选择。
 * 如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2
 * ）可选。
 * 所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
 * 因此，玩家 1 永远不会成为赢家，返回 False 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：[1, 5, 233, 7]
 * 输出：True
 * 解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
 * ⁠    最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= 给定的数组长度 <= 20.
 * 数组里所有分数都为非负数且不会大于 10000000 。
 * 如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。
 * 
 * 
 */

// 极小极大的时间复杂度 O(2^n)
// 动态规划的时间复杂度 O(n^2) 优于极小极大。 不过这个题n<=20 看不出来

// 思路1 极小极大dfs遍历  6.67% 640ms。。。
// 递归实现  思想如下：
// 01 function minimax(node, depth, maximizingPlayer)
// 02     if depth = 0 or node is a terminal node
// 03         return the heuristic value of node

// 04     if maximizingPlayer
// 05         bestValue := −∞
// 06         for each child of node
// 07             v := minimax(child, depth − 1, FALSE)
// 08             bestValue := max(bestValue, v)
// 09         return bestValue

// 10     else    (minimizing player)
// 11         bestValue := +∞
// 12         for each child of node
// 13             v := minimax(child, depth − 1, TRUE)
// 14             bestValue := min(bestValue, v)
// 15         return bestValue

// 思路2 极大极小优化 224 ms 6.67% 使用index代替传入并且反复创建数组
// 思路3 简化代码 296 ms 6.67% 
// 思路4 思路3+记忆化 88ms 31%


// 思路5 DP  80 ms 44%
// 懂了极大极小算法之后 ，思考dp就不难了。
// DP就是从大到小的递归思考，但从小到大的解决。是一种不带重复的简单for循环。
// 来走起，尝试将极大极小问题思考为一个简单for循环，而非依靠递归。
// 定义 dp[i][j] i到j内  先手比后手高出多少分
// 初始化 dp[i][i] = nums[i]
// 状态转移方程 dp[i][j] = max(先手取左, 先手取右)
//                      = max(nums[i] - dp[i+1][j],  nums[j] - dp[i][j-1])
// 这里的实现，只计算上半个三角形的值，状态转移方向为左下得出右上角。
// 所以迭代的方向为从下到上，从左到右


// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */

// 思路1 极小极大dfs遍历  6.67% 640ms。。。
// function minMax(array, isMaxLayer) {
//     if (array.length == 0) return 0;
//     if (array.length == 1) return array[0];
//     if (array.length == 2) { // 注意没有这个分支将变成1244ms。。。
//         let diff = Math.abs(array[0] - array[1])
//         return isMaxLayer ? diff : -diff;
//     }


//     let useLeftArray = array.slice(1)
//     let useRightArray = array.slice(0, array.length - 1)

//     if (isMaxLayer) {
//         return Math.max(array[0] + minMax(useLeftArray, false),
//             array[array.length - 1] + minMax(useRightArray, false))
//     } else {
//         return Math.min(minMax(useLeftArray, true) - array[0],
//             minMax(useRightArray, true) - array[array.length - 1])
//     }
// }

// var PredictTheWinner = function (nums) {
//     return minMax(nums, true) >= 0;
// };


// 思路2 极大极小优化 224 ms 6.67% 使用index代替传入并且反复创建数组
// var PredictTheWinner = function (nums) {

//     function minMax(start, end, isMaxLayer) {
//         if (start > end) return 0;
//         if (start == end) return nums[start];
//         if (start == end - 1) {
//             let diff = Math.abs(nums[start] - nums[end])
//             return isMaxLayer ? diff : -diff;
//         }

//         if (isMaxLayer) {
//             return Math.max(nums[start] + minMax(start + 1, end, false),
//                 nums[end] + minMax(start, end - 1, false))
//         } else {
//             return Math.min(minMax(start + 1, end, true) - nums[start],
//                 minMax(start, end - 1, true) - nums[end])
//         }
//     }

//     return minMax(0, nums.length - 1, true) >= 0;
// };


// 思路3 简化代码，这里比较有趣的是Pick的代码 使用- 直接隐去了isMaxLayer的概念
// 296 ms	6.67%
// var PredictTheWinner = function (nums) {

//     const helper = (i, j) => { // i，j是两端的索引
//         if (i == j) {    // 递归的出口，此时只有一个选择，并且没有剩余的可选
//             return nums[i];
//         }
//         const pickI = nums[i] - helper(i + 1, j); // 选择左端
//         const pickJ = nums[j] - helper(i, j - 1); // 选择右端
//         return Math.max(pickI, pickJ);            // 取较大者
//     };

//     return helper(0, nums.length - 1) >= 0;
// };

// 思路4 记忆化 极大极小 88ms 31%
// const PredictTheWinner = (nums) => {
//     const len = nums.length;

//     const memo = new Array(len);
//     for (let i = 0; i < memo.length; i++) {
//         memo[i] = new Array(len);
//     }

//     const helper = (i, j) => { // i，j是两端的索引
//         if(memo[i][j] != undefined) return memo[i][j];

//         if (i == j) {    // 递归的出口，此时只有一个选择，并且没有剩余的可选
//             return nums[i];
//         }
//         const pickI = nums[i] - helper(i + 1, j); // 选择左端
//         const pickJ = nums[j] - helper(i, j - 1); // 选择右端
//         memo[i][j]  = Math.max(pickI, pickJ);     // 取较大者
//         return memo[i][j];
//     };

//     return helper(0, nums.length - 1) >= 0;
// }

// 思路5 dp 80 ms 44%
const PredictTheWinner = (nums) => {
    const len = nums.length
    const dp = new Array(len);
    for (let i = 0; i < len; i++) {
        dp[i] = new Array(len);
        dp[i][i] = nums[i];
    }

    for (let i = len - 2; i >= 0; i--) {
        for (let j = i + 1; j < len; j++) {
            dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        }
    }

    return dp[0][len - 1] >= 0
}


// @lc code=end

console.log(PredictTheWinner([1, 5, 2]))
// console.log(PredictTheWinner([1, 5, 233, 7]))
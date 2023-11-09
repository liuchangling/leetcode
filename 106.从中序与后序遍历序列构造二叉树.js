/*
 * @lc app=leetcode.cn id=106 lang=javascript
 *
 * [106] 从中序与后序遍历序列构造二叉树
 */

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

// @lc code=start
// 同105题
// 思路 后序遍历的最后一个节点 是根
// 在中序中找到根所在的位置，计算出左子树和右子树的个数
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function (inorder, postorder) {
  const m = new Map();
  inorder.forEach((value, key) => {
    m.set(value, key);
  });

  function findTree(il, ir, pl, pr) {
    if (il > ir) return null;

    const rootValue = postorder[pr];
    const root = m.get(rootValue);

    let ans = new TreeNode(rootValue);
    // 中序 ：左 il ... root-1 右 root+1...ir
    // 后序 ：左 pl  ? 右? ,pr -1
    // 计算后序的左边最右边节点下标。 左子树个数为 root-1 - il +1 = root -il 个
    const tempIndex = pl + root - il - 1;
    ans.left = findTree(il, root - 1, pl, tempIndex);
    ans.right = findTree(root + 1, ir, tempIndex + 1, pr-1);

    return ans;
  }

  const n = inorder.length - 1;
  return findTree(0, n, 0, n);
};
// @lc code=end

console.log(buildTree([9, 3, 15, 20, 7],  [9,15,7,20,3]));

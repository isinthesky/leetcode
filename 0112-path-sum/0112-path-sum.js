/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
  if (!root) return false;

  const depth = (node, leaf, targetNumber) => {
    if (node) {
      if (!node.left && !node.right) {
        if (targetNumber === leaf + node.val) {
          return true;
        }
      }

      if (node.left) {
        if(depth(node.left, leaf + node.val, targetSum)) {
          return true;
        }
      }

      if (node.right) {
        if (depth(node.right, leaf + node.val, targetSum)) {
          return true;
        }
      }
    }
  }

  return depth(root, 0, targetSum)? true : false;

};
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
 * @return {boolean}
 */
var isBalanced = function(root) {

  if (!root) return true;
  
  const Lcount = {depth: 0, max: 0};
  const Rcount = {depth: 0, max: 0};

  const getDepth = (node, count) => {
    if (node) {
      count.depth += 1;

      if (count.depth > count.max) {
        count.max = count.depth;
      }

      if (node.left) {
        getDepth(node.left, count);
        count.depth -= 1;
      }

      if (node.right) {
        getDepth(node.right, count);
        count.depth -= 1;
      }
    }
  }

  if (root.left) {
    getDepth(root.left, Lcount);
  }

  if (root.right) {
    getDepth(root.right, Rcount);
  }

  const gap = Math.abs(Lcount.max-Rcount.max);

  if (gap < 2) {
    if (root.left) {
      if (!isBalanced(root.left)) {
        return false;
      }
    }

    if (root.right) {
      if (!isBalanced(root.right)) {
        return false;
      } 
    }
  } else {
    return false;
  }
  
  return true;
};
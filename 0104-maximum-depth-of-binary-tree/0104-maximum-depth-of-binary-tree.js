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
 * @return {number}
 */
var maxDepth = function(root) {
    
  const count = {depth : 0, max : 0};

  const countDepth = (node, count) => {

    if (node) {
      count.depth += 1;

      if (count.depth > count.max) {
        count.max = count.depth;
      }

      if (node.left) {
        countDepth(node.left, count);
        count.depth -= 1;
      }

      if (node.right) {
        countDepth(node.right, count);
        count.depth -= 1;
      }
    }
  }

  countDepth(root, count);

  return count.max;
};
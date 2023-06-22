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
var minDepth = function(root) {
  if (!root) return 0;

  const leafObj = {depth: 0, leaf: []};

  const Depth = (node, count) => {
    if (node) {
      count.depth += 1;

      if(!node.left && !node.right) {
        count.leaf.push(count.depth);
      }

      if (node.left) {
        Depth(node.left, count);
        count.depth -= 1;
      }

      if (node.right) {
        Depth(node.right, count);
        count.depth -= 1;
      }
    }
  }

  Depth(root, leafObj);

  return  Math.min.apply(null, leafObj.leaf);
};
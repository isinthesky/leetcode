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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
  const values = [];

  const inorder = function(root, array) {
    if (root) {
      if (root.left) {
        inorder(root.left, array);
      }

      if (root.val != null) {
        array.push(root.val);
      }

       if (root.right) {
        inorder(root.right, array);
      }
    }
  } 

  inorder(root, values)

  return values;
};
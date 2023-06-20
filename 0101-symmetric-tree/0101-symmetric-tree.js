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
var isSymmetric = function(root) {

  const LArray = [];
  const RArray = [];
    
  const LTree = (node, array) => {
    if (node) {
      if (node.val) {
        array.push(node.val);
      }

      if (node.left) {
        LTree(node.left, array);
      } else {
        array.push(1);
      }

      if (node.right) {
        LTree(node.right, array);
      } else {
        array.push(2)
      }
    }
  }

  const RTree = (node, array) => {
    if (node) {
      if (node.val) {
        array.push(node.val);
      }

      if (node.right) {
        RTree(node.right, array);
      } else {
        array.push(1);
      }

      if (node.left) {
        RTree(node.left, array);
      } else {
        array.push(2);
      }
    }
  }

  if (root.left) {
    LTree(root.left, LArray);
  }

  if (root.right) {
    RTree(root.right, RArray);
  }

  if (LArray.length !== RArray.length) return false;

  for (let i = 0; i < LArray.length; i += 1) {
    if (LArray[i] !== RArray[i]) {
      return false;
    } 
  }

  return true;
};
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

  if (!root) return false;

  const isSame = (LNode, RNode) => {
    if (LNode && RNode) {
      if (LNode.val === RNode.val) {
        if (!LNode.left && !RNode.right && !LNode.right && !RNode.left) return true;

        if (LNode.left && RNode.right) {
          if (!isSame(LNode.left, RNode.right)) return false;
        } 
        
        if (LNode.right && RNode.left) {
          if (!isSame(LNode.right, RNode.left)) return false;
        }

        if ((!LNode.left && RNode.right) || (LNode.left && !RNode.right)) {
          return false;
        }

        if ((LNode.right && !RNode.left) || (!LNode.right && RNode.left)) {
          return false;
        }
      } else {  
        return false;
      }
    } else {
      return false;
    }
  
    return true;
  }

  if (!root.left && !root.right) return true;

  return isSame(root.left, root.right);
};
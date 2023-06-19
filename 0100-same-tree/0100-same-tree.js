/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {

  const pArray = [];
  const qArray = [];    

  const pTree = (node, array) => {
    if (node) {
      pArray.push(node.val);

      if (node.left) {
        pArray.push("L");
        pTree(node.left, array);
      } else {
      pArray.push("Err");
    }

      if (node.right) {
        pArray.push("R");
        pTree(node.right, array);
      } else {
        pArray.push("Err");
      }
    }
  }

  const qTree = (node, array) => {
    if (node) {
      qArray.push(node.val);

      if (node.left) {
        qArray.push("L");
        qTree(node.left, array);
      } else {
        qArray.push("Err");
      }

      if (node.right) {
        qArray.push("R");
        qTree(node.right, array);
      } else {
        qArray.push("Err");
      }
    }
  }

  pTree(p,pArray);
  qTree(q,qArray);

console.log(pArray, qArray);


  if (pArray.length !== qArray.length) return false;

  for (let i = 0; i < pArray.length; i += 1 ) {
    if (pArray[i] !== qArray[i]) {
      return false;
    }
  }

  return true;
};

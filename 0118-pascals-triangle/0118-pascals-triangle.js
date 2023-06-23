/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
  const result = [[1]];

  for (let i = 1; i < numRows; i += 1) {
    result.push([]);

    for (let j = 0; j <= i; j += 1) {
      result[i].push((result[i-1][j - 1] ? result[i-1][j - 1] : 0) + (result[i-1][j] ? result[i-1][j] : 0));
    }
  }

  return result;
};
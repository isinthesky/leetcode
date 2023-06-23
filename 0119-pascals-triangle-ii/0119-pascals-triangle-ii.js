/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
  const row = [[1]];

  for (let i = 1; i <= rowIndex; i += 1) {
    row.push([]);
    
    for (let j = 0; j <= i; j += 1) {
      row[i].push((row[i-1][j-1] ? row[i-1][j-1] : 0) + (row[i-1][j] ? row[i-1][j] : 0));
    }
  }

  return row[rowIndex];
};
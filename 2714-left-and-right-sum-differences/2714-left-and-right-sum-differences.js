/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRightDifference = function(nums) {
    const leftArr = [0];
    const rightArr = [0];
    const len = nums.length;

    nums.slice(0,len-1).reduce((acc, current) => {
        leftArr.push(acc + current);
        return acc + current;
    }, 0)

    const reverseNums = nums.reverse()

    reverseNums.slice(0,len-1).reduce((acc, current) => {
        rightArr.push(acc + current);
        return acc + current;
    }, 0)

    const revArr = rightArr.reverse();

    return leftArr.map((list, idx) => 
        Math.abs(list - revArr[idx])
    )
};
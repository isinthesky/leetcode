/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        
        const ret = nums.indexOf(target - nums[i], i + 1);
        if (ret >= 0) {
            return [i, ret];
        }
    }
};
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    const array = [0,1,2];

    if (3 > n){
        return array[n];
    }

    for (let i = 3; i <= n; i+=1){
        array.push(array[i-1] + array[i-2]); 
    }

    return array[n];
}
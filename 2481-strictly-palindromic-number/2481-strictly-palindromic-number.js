/**
 * @param {number} n
 * @return {boolean}
 */
var isStrictlyPalindromic = function(n) {
    for(let i=2; i <= n-2; i++) {
        const bin = n.toString(i);
        
        if(bin.split('').reverse().join('') !== bin) {
           return false;
        }
    }

    return true;
};
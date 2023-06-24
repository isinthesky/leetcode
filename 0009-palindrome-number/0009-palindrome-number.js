/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const str = String(x);
    
    for (let i = 0; i < str.length / 2; i += 1){
        if (str[i] !== str.at(-(i + 1))) {
            return false;
        }
    }

    return true;
};
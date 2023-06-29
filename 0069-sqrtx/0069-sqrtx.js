/**
 * @param {number} x
 * @return {number}
 */

 // s 2:7
var mySqrt = function(x) {

    let result = 0;

    while (true) {
        if (result * result === x) {
            return result
        }

         if (result * result > x) {
            return result - 1
        }

        result += 1;
    }
};
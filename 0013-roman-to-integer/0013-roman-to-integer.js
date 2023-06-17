/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let number = 0;
    for(let i = 0; i < s.length; i += 1) {
        switch(s[i]){
            case 'I':
            number += 1
            break;
            case 'V':
            number += (s[i - 1] === 'I') ? 3 : 5
            break;
            case 'X':
            number += (s[i - 1] === 'I') ? 8 : 10
            break;
            case 'L':
            number += (s[i - 1] === 'X') ? 30 : 50
            break;
            case 'C':
            number += (s[i - 1] === 'X') ? 80 : 100
            break;
            case 'D':
            number += (s[i - 1] === 'C') ? 300 : 500
            break;
            case 'M':
            number += (s[i - 1] === 'C') ? 800 : 1000
            break;   
        }
    }

    return number;
};
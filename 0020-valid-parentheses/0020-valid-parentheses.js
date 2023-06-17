/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];

    const bracket = new Map();
    bracket.set("(",")");
    bracket.set("[","]");
    bracket.set("{","}");
    
    for (let i = 0; i < s.length; i += 1 ){
        if(bracket.has(s[i])) {
            stack.push(s[i]);
        } else {
            if (0 >= stack.length) return false;

            if (bracket.get(stack.pop()) !== s[i]) return false;       
        }
    }

    if (stack.length !== 0) return false;

    return true;
};

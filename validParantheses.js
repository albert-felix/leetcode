/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
    let open = {'(': 1, '[': 2, '{': 3}
    let close = {')': 1, ']': 2, '}': 3}
    
    let check = []
    
    for (let i=0; i<s.length; i++){
        if(s[i] in open){
            check.push(open[s[i]])
        }
        else{
            if(close[s[i]] === check[check.length -1]){
                check.pop()
            }
            else{
                return false;
            }
        }
    }
    return check.length ? false : true
    
};

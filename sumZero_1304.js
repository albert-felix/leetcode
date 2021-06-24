/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    if(n === 1){
        return [0];
    }
    else if(n%2 === 0){
        let result = []
        for(let i=1; i <= (n/2); i++){
            result.push(-i, i)
        }
        return result;
    }
    else{
        let result = []
        for(let i=1; i <= Math.floor(n/2); i++){
            result.push(-i, i)
        }
        let lastValue = result.pop()
        result.push(lastValue+n, -n)
        return result;
    }
};

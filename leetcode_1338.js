/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    let half = arr.length/2
    let freq = {}
    let total = 0
    arr.forEach(value => {
        if(!(value in freq)){
            freq[value] = 0
        }
        freq[value] += 1
    })
    
    freqSorted = Object.values(freq).sort((a,b) => b-a)
    for(let i=0; i<freqSorted.length;i++){
        total += freqSorted[i]
        if(total >= half){
            return i+1
        }
    }
    return arr.length

};

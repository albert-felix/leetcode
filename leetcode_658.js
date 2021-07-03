/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findClosestElements = function(arr, k, x) {
    
    let l=0;
    let h=arr.length-k
    
    if(l === h){
        return arr
    }
    else{
        while(l<h){
            let m = Math.floor(l + (h-l)/2)
            if(x - arr[m] > arr[m+k] - x){
                l = m + 1
            }
            else{
                h = m
            }
            
        }
        return(arr.slice(l,l+k))
    }
    
    
}

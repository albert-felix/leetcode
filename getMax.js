/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    
    if (n === 0) {
        return(0)
    }
    let nums = [0,1]
    if (n > 2){
        for (let i=2; i<=n; i++) {
            if(i%2 === 0) {
                nums[i] = nums[Math.floor(i/2)]         
            }
            else{
                nums[i] = nums[Math.floor(i/2)] + nums[Math.floor(i/2) + 1]
            }
        
        }
    }
    return(Math.max(...nums))
};

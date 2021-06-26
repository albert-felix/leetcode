/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let lastReachIndex = nums.length -1;
    for(let i=nums.length-1; i>=0; i--){
        if(i + nums[i] >= lastReachIndex){
            lastReachIndex = i
        }
    }
    return lastReachIndex === 0;
};

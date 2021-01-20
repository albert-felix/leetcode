/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
  let result = []
  let sum = 0;
  nums.forEach((num) => {
      sum += num
      result.push(sum)
  })
  return(result)
};

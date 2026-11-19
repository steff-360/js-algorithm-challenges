// Reto: Maxima suma de subarray (Kadane's Algorithm)
// Dado un array de enteros, encuentra el subarray contiguo con la mayor suma.
// Ejemplo: maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) => 6

function maxSubArray(nums) {
  let maxSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }
  return maxSum;
}

console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])); // 6
console.log(maxSubArray([1]));                               // 1
console.log(maxSubArray([5, 4, -1, 7, 8]));                 // 23

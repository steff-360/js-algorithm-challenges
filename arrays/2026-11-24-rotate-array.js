// Rotar array k posiciones a la derecha - O(n)
function rotate(nums, k) {
  k = k % nums.length;
  reverse(nums, 0, nums.length - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, nums.length - 1);
  return nums;
}
function reverse(arr, lo, hi) {
  while (lo < hi) { [arr[lo], arr[hi]] = [arr[hi], arr[lo]]; lo++; hi--; }
}
console.log(rotate([1,2,3,4,5,6,7], 3)); // [5,6,7,1,2,3,4]

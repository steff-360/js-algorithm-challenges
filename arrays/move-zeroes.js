// Reto: Mover ceros al final
// Dado un array de enteros, mueve todos los 0s al final
// manteniendo el orden relativo de los demas elementos.
// Ejemplo: moveZeroes([0,1,0,3,12]) => [1,3,12,0,0]

function moveZeroes(nums) {
  let insertPos = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      nums[insertPos++] = nums[i];
    }
  }
  while (insertPos < nums.length) {
    nums[insertPos++] = 0;
  }
  return nums;
}

console.log(moveZeroes([0, 1, 0, 3, 12])); // [1, 3, 12, 0, 0]
console.log(moveZeroes([0, 0, 1]));         // [1, 0, 0]

// Transponer matriz NxM - O(n*m)
function transpose(matrix) {
  return matrix[0].map((_, colIdx) => matrix.map(row => row[colIdx]));
}
const m = [[1,2,3],[4,5,6],[7,8,9]];
console.log(transpose(m));
// [[1,4,7],[2,5,8],[3,6,9]]

// Fibonacci con memoizacion - O(n)
const fib = (() => {
  const cache = {};
  return function f(n) {
    if (n <= 1) return n;
    return cache[n] ?? (cache[n] = f(n - 1) + f(n - 2));
  };
})();
console.log([...Array(10).keys()].map(fib));
// [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

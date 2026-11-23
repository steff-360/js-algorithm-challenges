// Memoize generico para cualquier funcion pura
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}
const expensiveAdd = memoize((a, b) => { console.log('calculando...'); return a + b; });
expensiveAdd(2, 3); // calculando... -> 5
expensiveAdd(2, 3); // desde cache  -> 5

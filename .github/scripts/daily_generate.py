import datetime, os, sys

colombia_tz = datetime.timezone(datetime.timedelta(hours=-5))
now_col = datetime.datetime.now(colombia_tz)
today = now_col.date()
date_str = today.isoformat()
idx = (now_col.timetuple().tm_yday - 1) % 15

challenges = [
    ("recursion", "fibonacci-memoized.js", """\
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
"""),
    ("arrays", "binary-search.js", """\
// Binary Search - O(log n)
function binarySearch(arr, target) {
  let lo = 0, hi = arr.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid] === target) return mid;
    arr[mid] < target ? (lo = mid + 1) : (hi = mid - 1);
  }
  return -1;
}
console.log(binarySearch([1,3,5,7,9,11], 7)); // 3
console.log(binarySearch([1,3,5,7,9,11], 4)); // -1
"""),
    ("arrays", "flatten-deep.js", """\
// Aplanar array anidado a cualquier profundidad
function flattenDeep(arr) {
  return arr.reduce((acc, val) =>
    Array.isArray(val) ? acc.concat(flattenDeep(val)) : acc.concat(val), []);
}
console.log(flattenDeep([1,[2,[3,[4]],5]])); // [1,2,3,4,5]
"""),
    ("functions", "debounce.js", """\
// Debounce: retrasa la ejecucion hasta que pare de llamarse
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
const log = debounce((msg) => console.log(msg), 300);
log('a'); log('b'); log('c'); // solo imprime 'c'
"""),
    ("functions", "throttle.js", """\
// Throttle: ejecuta maximo una vez por intervalo
function throttle(fn, interval) {
  let last = 0;
  return function(...args) {
    const now = Date.now();
    if (now - last >= interval) {
      last = now;
      return fn.apply(this, args);
    }
  };
}
"""),
    ("objects", "deep-clone.js", """\
// Deep clone sin referencias compartidas
function deepClone(obj) {
  if (obj === null || typeof obj !== 'object') return obj;
  if (Array.isArray(obj)) return obj.map(deepClone);
  return Object.fromEntries(Object.entries(obj).map(([k, v]) => [k, deepClone(v)]));
}
const a = { x: 1, y: { z: [2, 3] } };
const b = deepClone(a);
b.y.z.push(99);
console.log(a.y.z); // [2, 3] - sin mutacion
"""),
    ("strings", "valid-parentheses.js", """\
// Validar que los parentesis esten correctamente cerrados
function isValid(s) {
  const map = { ')': '(', ']': '[', '}': '{' };
  const stack = [];
  for (const ch of s) {
    if ('([{'.includes(ch)) stack.push(ch);
    else if (stack.pop() !== map[ch]) return false;
  }
  return stack.length === 0;
}
console.log(isValid('()[]{}')); // true
console.log(isValid('([)]'));   // false
"""),
    ("arrays", "chunk-array.js", """\
// Dividir array en trozos de tamano n
function chunk(arr, size) {
  const result = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}
console.log(chunk([1,2,3,4,5], 2)); // [[1,2],[3,4],[5]]
"""),
    ("objects", "group-by.js", """\
// Agrupar array de objetos por una clave
function groupBy(arr, key) {
  return arr.reduce((acc, item) => {
    const group = typeof key === 'function' ? key(item) : item[key];
    (acc[group] ??= []).push(item);
    return acc;
  }, {});
}
const people = [{name:'Ana',dept:'Dev'},{name:'Luis',dept:'QA'},{name:'Sara',dept:'Dev'}];
console.log(groupBy(people, 'dept'));
"""),
    ("strings", "longest-no-repeat.js", """\
// Substring mas largo sin caracteres repetidos - Sliding Window O(n)
function lengthOfLongestSubstring(s) {
  const seen = new Map();
  let max = 0, start = 0;
  for (let i = 0; i < s.length; i++) {
    if (seen.has(s[i]) && seen.get(s[i]) >= start) start = seen.get(s[i]) + 1;
    seen.set(s[i], i);
    max = Math.max(max, i - start + 1);
  }
  return max;
}
console.log(lengthOfLongestSubstring('abcabcbb')); // 3
console.log(lengthOfLongestSubstring('pwwkew'));    // 3
"""),
    ("functions", "compose.js", """\
// Composicion de funciones (derecha a izquierda)
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe    = (...fns) => x => fns.reduce((acc, fn)       => fn(acc), x);

const double = x => x * 2;
const inc    = x => x + 1;
const square = x => x * x;

console.log(compose(square, inc, double)(3)); // square(inc(double(3))) = 49
console.log(pipe(double, inc, square)(3));    // square(inc(double(3))) = 49
"""),
    ("functions", "memoize.js", """\
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
"""),
    ("arrays", "rotate-array.js", """\
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
"""),
    ("arrays", "remove-duplicates.js", """\
// Eliminar duplicados manteniendo orden de aparicion
const unique = arr => [...new Set(arr)];
// Por propiedad de objetos
const uniqueBy = (arr, key) => [...new Map(arr.map(x => [x[key], x])).values()];

console.log(unique([1,2,2,3,1,4])); // [1,2,3,4]
const users = [{id:1,name:'Ana'},{id:2,name:'Luis'},{id:1,name:'Ana Dup'}];
console.log(uniqueBy(users, 'id')); // [{id:1,...},{id:2,...}]
"""),
    ("arrays", "matrix-transpose.js", """\
// Transponer matriz NxM - O(n*m)
function transpose(matrix) {
  return matrix[0].map((_, colIdx) => matrix.map(row => row[colIdx]));
}
const m = [[1,2,3],[4,5,6],[7,8,9]];
console.log(transpose(m));
// [[1,4,7],[2,5,8],[3,6,9]]
"""),
]

folder, name, content = challenges[idx]
os.makedirs(folder, exist_ok=True)
base_target = os.path.join(folder, f"{date_str}-{name}")
target = base_target
v = 2
while os.path.exists(target):
    target = os.path.join(folder, f"{date_str}-v{v}-{name}")
    v += 1
with open(target, "w") as f:
    f.write(content)
print(f"Created: {target}")

// Composicion de funciones (derecha a izquierda)
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe    = (...fns) => x => fns.reduce((acc, fn)       => fn(acc), x);

const double = x => x * 2;
const inc    = x => x + 1;
const square = x => x * x;

console.log(compose(square, inc, double)(3)); // square(inc(double(3))) = 49
console.log(pipe(double, inc, square)(3));    // square(inc(double(3))) = 49

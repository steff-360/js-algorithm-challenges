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

// Eliminar duplicados manteniendo orden de aparicion
const unique = arr => [...new Set(arr)];
// Por propiedad de objetos
const uniqueBy = (arr, key) => [...new Map(arr.map(x => [x[key], x])).values()];

console.log(unique([1,2,2,3,1,4])); // [1,2,3,4]
const users = [{id:1,name:'Ana'},{id:2,name:'Luis'},{id:1,name:'Ana Dup'}];
console.log(uniqueBy(users, 'id')); // [{id:1,...},{id:2,...}]

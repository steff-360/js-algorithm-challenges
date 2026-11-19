// Reto: Palindromo
// Verifica si una cadena es palindromo ignorando espacios y mayusculas.
// Ejemplo: isPalindrome("A man a plan a canal Panama") => true

function isPalindrome(s) {
  const clean = s.toLowerCase().replace(/[^a-z0-9]/g, '');
  return clean === clean.split('').reverse().join('');
}

// Reto: Anagrama
// Verifica si dos cadenas son anagramas entre si.
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const count = {};
  for (const char of s) count[char] = (count[char] || 0) + 1;
  for (const char of t) {
    if (!count[char]) return false;
    count[char]--;
  }
  return true;
}

// Reto: Capitalizar palabras
function capitalizeWords(str) {
  return str.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' ');
}

console.log(isPalindrome('A man a plan a canal Panama')); // true
console.log(isAnagram('anagram', 'nagaram'));              // true
console.log(capitalizeWords('hola mundo desde javascript')); // Hola Mundo Desde Javascript

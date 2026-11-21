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

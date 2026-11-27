# Last updated: 11/26/2026, 7:27:57 PM
1class Solution:
2    def countVowelSubstrings(self, word: str) -> int:
3        vowels = {'a', 'e', 'i', 'o', 'u'}
4        count = 0
5
6        for i in range (len(word)):
7            seen = set()
8
9            for j in range(i, len(word)):
10                if word[j] not in vowels:
11                    break
12                
13                seen.add(word[j])
14
15                if len(seen) == 5:
16                    count += 1
17
18        return count
# Last updated: 11/26/2026, 7:32:19 PM
1class Solution:
2    def countVowelSubstrings(self, word: str) -> int:
3        vowels = {'a', 'e', 'i', 'o', 'u'}
4        count = 0
5
6        for i in range (len(word)): #i is the starting pos of our substring
7            seen = set() 
8
9            for j in range(i, len(word)): #j is the ending pos of our substring
10                if word[j] not in vowels: #breaks if consonants is spotted
11                    break
12                
13                seen.add(word[j]) #if not a consonant, ass the current vowel to our set
14
15                if len(seen) == 5: #checks length to check if substring is valid
16                    count += 1
17
18        return count
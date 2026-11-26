# Last updated: 11/26/2026, 1:58:08 PM
1from collections import Counter
2
3class Solution:
4    def robotWithString(self, s: str) -> str:
5        count = Counter(s)
6        stack = []
7        result = []
8
9        for char in s:
10            stack.append(char)
11            count[char] -= 1
12
13            if count[char] == 0:
14                del count[char]
15
16            smallest = min(count) if count else "{"
17
18            while stack and stack[-1] <= smallest:
19                result.append(stack.pop())
20
21        return "".join(result)
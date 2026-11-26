# Last updated: 11/26/2026, 3:00:23 PM
1class Solution:
2    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
3        n = len(maxHeights)
4        left = [0] * n
5        right = [0] * n
6        stack = []
7
8        # Left side
9        for i in range(n):
10            while stack and maxHeights[stack[-1]] > maxHeights[i]:
11                stack.pop()
12
13            if stack:
14                j = stack[-1]
15                left[i] = left[j] + (i - j) * maxHeights[i]
16            else:
17                left[i] = (i + 1) * maxHeights[i]
18
19            stack.append(i)
20
21        stack = []
22
23        # Right side
24        for i in range(n - 1, -1, -1):
25            while stack and maxHeights[stack[-1]] > maxHeights[i]:
26                stack.pop()
27
28            if stack:
29                j = stack[-1]
30                right[i] = right[j] + (j - i) * maxHeights[i]
31            else:
32                right[i] = (n - i) * maxHeights[i]
33
34            stack.append(i)
35
36        # Find the maximum total
37        result = 0
38
39        for i in range(n):
40            total = left[i] + right[i] - maxHeights[i]
41            result = max(result, total)
42
43        return result
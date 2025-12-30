// Last updated: 12/30/2025, 6:42:21 PM
1class Solution {
2    public boolean isAnagram(String s, String t) {
3
4        if (s.length() != t.length())
5        {
6            return false; 
7        }
8
9        if(s.length() == t.length())
10        {
11            Map<Character, Integer> letters = new HashMap<>();
12
13            for (char chars : s.toCharArray())
14            {
15                letters.put(chars, letters.getOrDefault(chars, 0) + 1);
16            }
17
18            for (char chars : t.toCharArray())
19            {
20                letters.put(chars, letters.getOrDefault(chars, 0) - 1);
21            }
22
23            for (Integer chars : letters.values())
24            {
25                if (chars != 0)
26                {
27                    return false;
28                }
29            }
30        }
31        return true;
32    }
33}
34
35/* 
36        check if the strings are the same length, if it's not return false
37        if they are the same length, create a new hashmap 
38        for loop to iterate through each string s and keep track of the occurances of each value
39        then repeat for string t and subtract count from the letter
40        if all values are equal to 0 then return true 
41        if not return false
42*/
43
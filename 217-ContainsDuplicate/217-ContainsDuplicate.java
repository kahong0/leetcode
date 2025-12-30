// Last updated: 12/30/2025, 5:24:54 PM
1import java.util.HashSet;
2
3class Solution {
4    public boolean containsDuplicate(int[] nums) {
5        HashSet<Integer> set = new HashSet<>();
6
7        for (int n : nums) {
8            if (set.contains(n)) {
9                return true; // duplicate found
10            }
11            set.add(n);
12        }
13
14        return false; // no duplicates
15    }
16}
17

  /*create a hashset 
    create a for loop to loop through the array 
    for each iteration add the unique value in the hashset 
    if a number is already in the hashset, then program returns false 
    if all numbers are added in the hashset, then return true
  */

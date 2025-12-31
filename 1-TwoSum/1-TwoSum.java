// Last updated: 12/31/2025, 1:02:26 PM
1class Solution {
2    public int[] twoSum(int[] nums, int target) {
3
4        int n = nums.length;
5
6        for (int i = 0; i < n; i++) 
7        {  
8            for (int j = i + 1; j < n; j++)
9            {
10            if (nums[i] + nums[j] == target)
11                {
12                return new int[]{i,j};
13                }
14            }
15        }
16        return new int[]{ , };
17    }
18}
19
20/* 
21create a for-loop and trace through each value in the array 
22take the value at the first index and add it the value at the following index and see if it adds up to the target
23if it doesn't add it the target continue to the next value
24once you get to the end of the array, loop back to the next index and compare the rest
25*/
26
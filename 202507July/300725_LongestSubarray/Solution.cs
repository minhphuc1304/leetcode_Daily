public class Solution {
    public int LongestSubarray(int[] nums) {
        int n = nums.Length;
        
        // 1) Find global max
        int maxA = nums[0];
        for (int i = 1; i < n; i++) {
            if (nums[i] > maxA) 
                maxA = nums[i];
        }
        
        // 2) Count longest contiguous run where (v & maxA) == maxA
        int res = 0, c = 0;
        for (int i = 0; i < n; i++) {
            if ((nums[i] & maxA) == maxA) {
                c++;
                if (c > res) 
                    res = c;
            } else {
                c = 0;
            }
        }
        
        return res;
    }
}

public class Solution {
    public int CountMaxOrSubsets(int[] nums) {
        int maxOr = 0;
        for(int i=0; i<nums.Length; i++)
        {
            maxOr = maxOr | nums[i];
        }

        return GetCount(nums, 0, maxOr, 0);
    }

    private int GetCount(int[] nums, int or, int maxOr, int i)
    {
        if(i>=nums.Length)
        {
            return maxOr == or? 1 : 0;
        }

       return  GetCount(nums, or, maxOr, i+1) +
        GetCount(nums, or | nums[i], maxOr, i+1);
    }
}

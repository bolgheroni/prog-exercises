public class Solution {
    public int MaxSubArray(int[] nums) {
        // kadane's algorithm

        int maxEndingPrevious = nums[0];
        int maxUntilNow = nums[0];

        for (int i = 1 ; i< nums.Length; i++) {
            int value = nums[i];
            int maxEndingNow = Math.Max(value, maxEndingPrevious + value);

            maxUntilNow = Math.Max(maxUntilNow, maxEndingNow);
            maxEndingPrevious = maxEndingNow;
        }

        return maxUntilNow;
    }
}
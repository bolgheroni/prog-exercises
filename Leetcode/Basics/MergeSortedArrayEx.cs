public class MergeSortedArrayEx {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int nums1Left = m -1;
        int nums2Left = n -1;

        // every iteration we subcract from one of them
        // n + m iterations
        while (nums1Left >= 0 || nums2Left >= 0) {
            int value;
            if (nums1Left < 0) {
                value = nums2[nums2Left];
                nums2Left--;
            } else if (nums2Left < 0) {
                value = nums1[nums1Left];
                nums1Left--;
            } else {
                // there are numbers left in both
                value = Math.Max(nums1[nums1Left], nums2[nums2Left]);
                if (value == nums1[nums1Left]) {
                    nums1Left--;
                } else {
                    nums2Left--;
                }
            }
            // we store at the end of nums1 arr
            nums1[nums1Left + nums2Left + 2] = value;
        }
    }
}

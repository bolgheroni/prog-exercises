public class MergeSortedArrayEx {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int[] newArr = new int[n + m];
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < m || j < n) {
            int value;
            if (i >= m) {
                value = nums2[j];
                j++;
            } else if (j >= n) {
                value = nums1[i];
                i++;
            } else {
                value = Math.Min(nums1[i], nums2[j]);
                if (value == nums1[i]) {
                    i++;
                } else {
                    j++;
                }
            }
            newArr[k] = value;
            k++;
        }
        for (int l =0; l < m +n; l++) {
            nums1[l] = newArr[l];
        }
    }
}
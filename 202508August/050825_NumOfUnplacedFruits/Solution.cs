public class Solution {
    public int NumOfUnplacedFruits(int[] fruits, int[] baskets) {
        int count = 0;
        int n = baskets.Length;
        foreach (int fruit in fruits) {
            int unplaced = 1;
            for (int i = 0; i < n; i++) {
                if (fruit <= baskets[i]) {
                    baskets[i] = 0;
                    unplaced = 0;
                    break;
                }
            }
            count += unplaced;
        }
        return count;
    }
}

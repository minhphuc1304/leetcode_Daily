public class Solution {
    public int MaxTotalFruits(int[][] fruits, int startPos, int k) {
        const int N = 200000;
        int[] pos = new int[N + 1];
        int ans = 0;

        // Populate the pos array with fruit amounts
        foreach (var fruit in fruits) {
            pos[fruit[0]] = fruit[1];
        }

        // Calculate prefix sums
        for (int i = 1; i <= N; i++) {
            pos[i] += pos[i - 1];
        }

        // Check for leftward movements
        for (int i = startPos; i >= Math.Max(startPos - k, 0); i--) {
            int dist = startPos - i;
            int R = startPos + (k - 2 * dist);
            ans = Math.Max(ans, (pos[startPos] - (i > 0 ? pos[i - 1] : 0)) + (pos[Math.Min(R, N)] - pos[startPos]));
        }

        // Check for rightward movements
        for (int i = startPos; i <= Math.Min(startPos + k, N); i++) {
            int dist = i - startPos;
            int R = startPos - (k - 2 * dist);
            int rv = (pos[i] - (startPos > 0 ? pos[startPos - 1] : 0));
            int lv = (startPos > 0 && R > 0) ? pos[startPos - 1] - pos[R - 1] : (startPos > 0 ? pos[startPos - 1] : 0);
            ans = Math.Max(ans, rv + lv);
        }

        return ans;
    }
}

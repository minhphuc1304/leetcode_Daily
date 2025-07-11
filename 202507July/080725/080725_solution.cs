public class Solution {
    public int MaxValue(int[][] events, int k) {
        Array.Sort(events, (a, b) => a[0] - b[0]);
        int n = events.Length;

        int[][] dp = new int[k + 1][];
        for (int i = 0; i <= k; i++) {
            dp[i] = new int[n];
            Array.Fill(dp[i], -1);
        }

        return DFS(0, k, events, dp);
    }

    private int DFS(int curIndex, int count, int[][] events, int[][] dp) {
        if (count == 0 || curIndex == events.Length) {
            return 0;
        }

        if (dp[count][curIndex] != -1) {
            return dp[count][curIndex];
        }

        int nextIndex = BisectRight(events, events[curIndex][1]);
        dp[count][curIndex] = Math.Max(DFS(curIndex + 1, count, events, dp), events[curIndex][2] + DFS(nextIndex, count - 1, events, dp));
        return dp[count][curIndex];
    }

    public static int BisectRight(int[][] events, int target) {
        int left = 0, right = events.Length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (events[mid][0] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}

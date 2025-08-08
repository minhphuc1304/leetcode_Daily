public class Solution
{
    public int MaxCollectedFruits(int[][] fruits)
    {
        int n = fruits.Length;
        if (n == 0) return 0;
        if (n == 1) return fruits[0][0];

        long ans = 0;
        for (int i = 0; i < n; ++i) ans += fruits[i][i];

        long Dp(int[][] a)
        {
            const long NEG = long.MinValue / 4; // safe sentinel
            long[] prev = Enumerable.Repeat(NEG, n).ToArray();
            long[] curr = new long[n];

            prev[n - 1] = a[0][n - 1];

            for (int i = 1; i < n - 1; ++i)
            {
                Array.Fill(curr, NEG);
                int start = Math.Max(n - 1 - i, i + 1);
                for (int j = start; j < n; ++j)
                {
                    long best = prev[j];
                    if (j - 1 >= 0) best = Math.Max(best, prev[j - 1]);
                    if (j + 1 < n) best = Math.Max(best, prev[j + 1]);
                    if (best == NEG) continue; // unreachable
                    curr[j] = best + a[i][j];
                }
                // swap
                var tmp = prev; prev = curr; curr = tmp;
            }
            return prev[n - 1];
        }

        ans += Dp(fruits);

        // transpose in-place (upper triangle swap)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j)
                (fruits[j][i], fruits[i][j]) = (fruits[i][j], fruits[j][i]);

        ans += Dp(fruits);

        // If you must return int, clamp to int range.
        if (ans > int.MaxValue) return int.MaxValue;
        if (ans < int.MinValue) return int.MinValue;
        return (int)ans;
    }
}

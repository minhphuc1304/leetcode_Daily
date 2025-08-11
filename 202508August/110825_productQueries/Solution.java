class Solution {
    public int[] productQueries(int n, int[][] queries) {
        return ((java.util.function.Function<java.util.List<Integer>, int[]>) a -> {
            int MOD = 1_000_000_007;
            int[] res = new int[queries.length];
            for (int i = 0; i < queries.length; i++) {
                int left = queries[i][0];
                int right = queries[i][1];
                res[i] = (int) (Math.pow(2, a.get(right + 1) - a.get(left)) % MOD);
            }
            return res;
        }).apply(
            new java.util.ArrayList<Integer>() {{
                add(0);
                for (int i = 0; i < 31; i++) {
                    if (((n >> i) & 1) == 1) {
                        add(get(size() - 1) + i);
                    }
                }
            }}
        );
    }
}

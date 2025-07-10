class maxFreeTime_II {
    public int maxFreeTime(int eventTime, int[] startTime, int[] endTime) {
        int n = startTime.length;
        int[] gapsArr = new int[n + 1];
        int left = 0;

        for (int i = 0; i < n; i++) {
            gapsArr[i] = startTime[i] - left;
            left = endTime[i];
        }

        gapsArr[n] = eventTime - endTime[n - 1];

        int[] maxGapPrefix = new int[n];
        int[] maxGapSuffix = new int[n];

        maxGapPrefix[0] = gapsArr[0];
        maxGapSuffix[n - 1] = gapsArr[n];

        for (int i = 1; i < n; i++) {
            maxGapPrefix[i] = Math.max(maxGapPrefix[i - 1], gapsArr[i]);
        }

        for (int i = n - 2; i >= 0; i--) {
            maxGapSuffix[i] = Math.max(maxGapSuffix[i + 1], gapsArr[i + 1]);
        }
        
        int ans = 0;
        
        for (int i = 0; i < n; i++) {
            int curr = gapsArr[i] + gapsArr[i + 1];
            int barSize = endTime[i] - startTime[i];
            boolean isValid = false;
            
            if (i - 1 >= 0 && maxGapPrefix[i - 1] >= barSize) isValid = true;
            if (i + 1 < n && maxGapSuffix[i + 1] >= barSize) isValid = true;

            if (isValid) curr += barSize;
            ans = Math.max(ans, curr);
        }

        return ans;
    }

    public static void main(String[] args) {
        maxFreeTime_II sol = new maxFreeTime_II();

        int[] eventTime = {20, 5, 10, 10, 5};
        int[] expected = {8, 2, 7, 6, 0};
        int[][] startTime = {
            {2, 8, 14},
            {1, 3},
            {0, 7, 9},
            {0, 3, 7, 9},
            {0, 1, 2, 3, 4}
        };
        int[][] endTime = {
            {6, 10, 18},
            {2, 5},
            {1, 8, 10},
            {1, 4, 8, 10},
            {1, 2, 3, 4, 5}
        };

        for (int i = 0; i < eventTime.length; i++) {
            int result = sol.maxFreeTime(eventTime[i], startTime[i], endTime[i]);
            if (result == expected[i]) {
                System.out.println("Test case #" + (i + 1) + ": PASS");
            } else {
                System.out.println("Test case #" + (i + 1) + ": FAIL (got " + result + ", expected " + expected[i] + ")");
            }
        }
    }
}


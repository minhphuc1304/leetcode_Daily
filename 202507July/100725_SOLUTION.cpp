class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        vector<int> gapsArr;
        int left = 0;

        for (int i = 0; i < n; ++i) {
            int gap = startTime[i] - left;
            gapsArr.push_back(gap);
            left = endTime[i];
        }

        gapsArr.push_back(eventTime - endTime[n - 1]);

        vector<int> maxGapPrefix(n, 0), maxGapSuffix(n, 0);
        maxGapPrefix[0] = gapsArr[0];
        maxGapSuffix[n - 1] = gapsArr[n];

        for (int i = 1; i < n; ++i) {
            maxGapPrefix[i] = max(maxGapPrefix[i - 1], gapsArr[i]);
        }

        for (int i = n - 2; i >= 0; --i) {
            maxGapSuffix[i] = max(maxGapSuffix[i + 1], gapsArr[i + 1]);
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int curr = gapsArr[i] + gapsArr[i + 1];
            int barSize = endTime[i] - startTime[i];
            bool isValid = false;

            if (i - 1 >= 0 && maxGapPrefix[i - 1] >= barSize) isValid = true;
            if (i + 1 < n && maxGapSuffix[i + 1] >= barSize) isValid = true;

            if (isValid) curr += barSize;
            ans = max(ans, curr);
        }

        return ans;
    }
};

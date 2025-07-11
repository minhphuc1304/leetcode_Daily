#include <iostream>
#include <vector>
using namespace std;

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

int main() {
    Solution sol;

    vector<vector<int>> startTimes = {
        {2, 8, 14},
        {1, 3},
        {0, 7, 9},
        {0, 3, 7, 9},
        {0, 1, 2, 3, 4}
    };

    vector<vector<int>> endTimes = {
        {6, 10, 18},
        {2, 5},
        {1, 8, 10},
        {1, 4, 8, 10},
        {1, 2, 3, 4, 5}
    };

    vector<int> eventTimes = {20, 5, 10, 10, 5};
    vector<int> expected = {8, 2, 7, 6, 0};

    for (size_t i = 0; i < eventTimes.size(); ++i) {
        int result = sol.maxFreeTime(eventTimes[i], startTimes[i], endTimes[i]);
        if (result == expected[i]) {
            cout << "Test case #" << (i + 1) << ": PASS" << endl;
        } else {
            cout << "Test case #" << (i + 1) << ": FAIL (got " << result << ", expected " << expected[i] << ")" << endl;
        }
    }
    return 0;
}
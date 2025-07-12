#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>


using namespace std;

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        // Sort the meetings based on start time
        sort(meetings.begin(), meetings.end());
        
        // Min-heap of available rooms (stores room index)
        priority_queue<int, vector<int>, greater<>> available;
        for (int i = 0; i < n; ++i) {
            available.push(i);
        }

        // Min-heap for busy rooms (stores {end_time, room_index})
        using T = pair<long long, int>;
        priority_queue<T, vector<T>, greater<>> busy;

        vector<int> count(n, 0); // Count how many meetings each room held
        
        for (auto& meeting: meetings) {
            long long start = meeting[0];
            long long end = meeting[1];

            while (!busy.empty() && busy.top().first <= start) {
                auto [end_time, room] = busy.top(); busy.pop();
                available.push(room);
            }

            if (!available.empty()) {
                // If there is a free room, assign it to the meeting
                int room = available.top(); available.pop();
                busy.push({end, room});
                count[room]++;
            } else {
                // No room available -> delay the meeting
                auto [end_time, room] = busy.top(); busy.pop();
                long long duration = end - start;
                long long new_end = end_time + duration;
                busy.push({new_end, room});
                count[room]++;
            }
        }

        // Find the room that held the most meetings (prefer smaller index if tie)
        int maxCount = 0, result = 0;
        for (int i = 0; i < n; ++i) {
            if (count[i] > maxCount) {
                maxCount = count[i];
                result = i;
            }
        }

        return result;
    }
};


int main() {
    Solution sol;

    vector<tuple<int, vector<vector<int>>, int>> test_cases = {
        {2, {{0, 10}, {1, 5}, {2, 7}, {3, 4}}, 0},
        {3, {{1, 20}, {2, 10}, {3, 5}, {4, 9}, {6, 8}}, 1}
    };

    for (int i = 0; i < test_cases.size(); ++i) {
        auto [n, meetings, expected] = test_cases[i];
        int result = sol.mostBooked(n, meetings);
        if (result == expected)
            cout << "Test case #" << (i + 1) << ": PASS" << endl;
        else 
            cout << "Test case #" << (i+1) << ": FAIL (got " << result << ")" << endl;
    }

    return 0;
}
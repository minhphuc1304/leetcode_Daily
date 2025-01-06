#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> arr;
        for (int i = 0; i < n; i++) {
            int index = i + 1;
            int sum = 0;
            for (int j = 0; j < n; j++) {
                if (boxes[j] == '1' && (index - 1) != j) {
                    sum += abs(index - (j + 1));
                }
            }
            arr.push_back(sum);
        }
        return arr;
    }
};

void test() {
    Solution s;
    
}
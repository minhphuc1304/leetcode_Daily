#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char, vector<int>> mp;
        int ans = 0;

        // Lưu các vị trí xuất hiện của từng ký tự
        for (int i = 0; i < s.length(); i++) {
            mp[s[i]].push_back(i);
        }

        // Duyệt qua từng ký tự trong map
        for (auto &pair : mp) {
            int size = pair.second.size();
            if (size > 1) {
                // Lấy vị trí đầu (l) và cuối (r) của ký tự
                int l = pair.second[0], r = pair.second[size - 1];
                if (r - l > 1) {
                    // Kiểm tra các ký tự giữa l và r
                    unordered_set<char> vis;
                    for (int j = l + 1; j < r; j++) {
                        vis.insert(s[j]);
                    }
                    ans += vis.size(); // Thêm số ký tự duy nhất
                }
            }
        }

        return ans;
    }
};


void test() {
    Solution solution;

    // Test case 1
    string s1 = "aabca";
    int expected1 = 2;
    cout << "Test case 1: " << (solution.countPalindromicSubsequence(s1) == expected1 ? "Passed" : "Failed") << endl;

    // Test case 2
    string s2 = "abc";
    int expected2 = 0; // Không có subsequence palindrome nào
    cout << "Test case 2: " << (solution.countPalindromicSubsequence(s2) == expected2 ? "Passed" : "Failed") << endl;

    // Test case 3
    string s3 = "bbcbaba";
    int expected3 = 4; // Palindromes: "bbb", "bcb", "bab", "aba"
    cout << "Test case 3: " << (solution.countPalindromicSubsequence(s3) == expected3 ? "Passed" : "Failed") << endl;

    // Test case 4
    string s4 = "aaaa";
    int expected4 = 1; // Palindrome: "aaa"
    cout << "Test case 4: " << (solution.countPalindromicSubsequence(s4) == expected4 ? "Passed" : "Failed") << endl;

    // Test case 5
    string s5 = "abca";
    int expected5 = 1; // Palindrome: "aba"
    cout << "Test case 5: " << (solution.countPalindromicSubsequence(s5) == expected5 ? "Passed" : "Failed") << endl;
}

int main() {
    test();
    return 0;
}

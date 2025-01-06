// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/

#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char, vector<int>> mp;
        int ans = 0;

        for(int i = 0; i < s.length(); i++) {
            mp[s[i]].push_back(i);
        }

        for(auto &pair: mp) {
            int size = pair.second.size();
            if (size > 1) {
                int l = pair.second[0], r = pair.second[size - 1];
                if ( r - l > 1) {
                    vector<bool> vis(26, false);
                    for(int j = l + 1; j < r; j++) {
                        if(vis[s[j] - 'a']) continue;
                        ans++;
                        vis[s[j] - 'a'] = true;
                    }
                }
            }
        }

        return ans;
    }
};

void runTest(string testString, int expected) {
    Solution solution;
    int result = solution.countPalindromicSubsequence(testString);

    cout << "Input: \"" << testString << "\"\n";
    cout << "Output: " << result << "\n";
    cout << "Expected: " << expected << "\n";

    if (result == expected) {
        cout << "Test passed!\n\n";
    } else {
        cout << "Test failed!\n\n";
    }
}

int main() {
    // Test cases
    runTest("aabca", 3);          // Example case
    runTest("abc", 0);            // No valid palindromic subsequences
    runTest("aaa", 1);            // Only one unique palindromic subsequence: "aaa"
    runTest("abab", 2);           // Two unique palindromic subsequences: "aba", "bab"
    runTest("abacaba", 4);        // "aba", "aca", "bcb", "cac"
    runTest("aaaaa", 1);          // Only "aaa" is unique
    runTest("abcabc", 3);         // "aba", "bcb", "cac"
    runTest("a", 0);              // No valid palindromic subsequences
    runTest("ab", 0);             // No valid palindromic subsequences
    runTest("aabbcc", 3);         // "aba", "bcb", "cac"

    // Large test case
    string largeTest(100000, 'a');
    largeTest[0] = 'b';
    largeTest[99999] = 'c';
    runTest(largeTest, 1);        // Only "bcb" is possible

    return 0;
}
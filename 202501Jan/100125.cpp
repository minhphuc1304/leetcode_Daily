// 916. Word Subsets
// You are given two string arrays words1 and words2.

// A string b is a subset of string a if every letter in b occurs in a including multiplicity.

// For example, "wrr" is a subset of "warrior" but is not a subset of "world".
// A string a from words1 is universal if for every string b in words2, b is a subset of a.

// Return an array of all the universal strings in words1. You may return the answer in any order.

 

// Example 1:

// Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
// Output: ["facebook","google","leetcode"]
// Example 2:

// Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
// Output: ["apple","google","leetcode"]
 

// Constraints:

// 1 <= words1.length, words2.length <= 104
// 1 <= words1[i].length, words2[i].length <= 10
// words1[i] and words2[i] consist only of lowercase English letters.
// All the strings of words1 are unique.

#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

class Solution {
public:
    vector<string> wordSubsets(vector<string>& mainWords, vector<string>& requiredWords) {
        int maxCharFreq[26] = {0};
        int tempCharFreq[26];
        
        for (const auto& word : requiredWords) {
            memset(tempCharFreq, 0, sizeof tempCharFreq);//To Set Temp freq all to zero 
//You can do vector<int> tempCharFreq(26,0);
            for (char ch : word) {
                tempCharFreq[ch - 'a']++;
            }
            for (int i = 0; i < 26; ++i) {
                maxCharFreq[i] = max(maxCharFreq[i], tempCharFreq[i]);
            }
        }
        
        vector<string> universalWords;
        
        for (const auto& word : mainWords) {
            memset(tempCharFreq, 0, sizeof tempCharFreq);
            for (char ch : word) {
                tempCharFreq[ch - 'a']++;
            }
            bool isUniversal = true;
            for (int i = 0; i < 26; ++i) {
                if (maxCharFreq[i] > tempCharFreq[i]) {
                    isUniversal = false;
                    break;
                }
            }
            if (isUniversal) {
                universalWords.emplace_back(word);
            }
        }
        
        return universalWords;
    }
};

int main() {
    Solution solution;
    
    vector<string> mainWords1 = {"amazon", "apple", "facebook", "google", "leetcode"};
    vector<string> requiredWords1 = {"e", "o"};
    vector<string> result1 = solution.wordSubsets(mainWords1, requiredWords1);
    cout << "Test Case 1: ";
    for (const auto& word : result1) {
        cout << word << " ";
    }
    cout << endl;
    
    vector<string> mainWords2 = {"amazon", "apple", "facebook", "google", "leetcode"};
    vector<string> requiredWords2 = {"l", "e"};
    vector<string> result2 = solution.wordSubsets(mainWords2, requiredWords2);
    cout << "Test Case 2: ";
    for (const auto& word : result2) {
        cout << word << " ";
    }
    cout << endl;

    return 0;
}
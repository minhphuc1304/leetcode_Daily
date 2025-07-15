#include <iostream>
#include <string>
using namespace std;

class Solution_150725 {
    public: 
    bool isValid(string word) {
        if (word.length() < 3) return false;

        string vowels = "aeiouAEIOU";
        bool hasVowel = false;
        bool hasConsonant = false;
        
        for (char ch : word) {
            if (!isalnum(ch)) return false;

            if (isalpha(ch)) {
                if (vowels.find(ch) != string::npos) {
                    hasVowel = true;
                } else {
                    hasConsonant = true;
                }
            }
        }

        return hasVowel && hasConsonant;
    }
};

int main() {
    Solution_150725 sol;
    pair<string, bool> testCases[] = {
        {"abc", true},
        {"a1", false},
        {"123", false},
        {"aE3", false},
        {"bC5", false},
        {"Ae1", false},
        {"Bcd3", false},
        {"BcdE", true},
        {"abc#", false},
        {"aei", false},
        {"bcd", false},
        {"aBc1", true}
    };

    for (auto &[word, expected] : testCases) {
        bool result = sol.isValid(word);
        cout << "'" << word << "' ➜ " << (result ? "true" : "false")
             << " (expected: " << (expected ? "true" : "false") << ") "
             << (result == expected ? "✅" : "❌") << endl;
    }

    return 0;
}

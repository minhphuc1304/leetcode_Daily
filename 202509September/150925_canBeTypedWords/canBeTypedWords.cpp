class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        unordered_set<char> broken(brokenLetters.begin(), brokenLetters.end());
        int count = 0;
        istringstream iss(text);
        string word;
        while (iss >> word) {
            bool ok = true;
            for (char c : word) {
                if (broken.count(c)) { ok = false; break; }
            }
            if (ok) ++count;
        }
        return count;
    }
};

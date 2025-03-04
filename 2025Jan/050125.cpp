#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& Q) {
        int n = s.size();
        vector<int> A(n, 0);
        for(auto& it : Q) {
            int l = it[0];
            int r = it[1];
            int t = it[2];
            if (t == 1) {
                A[l] += 1;
                if (r + 1 < n) {
                    A[r + 1] -= 1;
                }
            } else {
                A[l] -= 1;
                if (r + 1 < n) {
                    A[r + 1] += 1;
                }
            }
        }
        for (int i = 1; i < n; ++i) {
            A[i] += A[i - 1];
        }
        for (int i = 0; i < n; ++i) {
            int shift = (A[i] % 26 + 26) % 26;
            int ch = s[i] - 'a';
            ch = (ch + shift) % 26;
            s[i] = 'a' + ch;
        }
        return s;
    }
};

void test() {
    
}
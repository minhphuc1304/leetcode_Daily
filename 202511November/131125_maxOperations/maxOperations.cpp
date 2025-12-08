class Solution {
public:
    int maxOperations(const string& s) {
        int a = 0;
        for (int i = s.size(), z = 0, p = 1; i--; ) {
            bool b = s[i] == '1';
            a += z & (!b-1);
            z += p & (b-1);
            p = b;
        }

        return a;
    }
};

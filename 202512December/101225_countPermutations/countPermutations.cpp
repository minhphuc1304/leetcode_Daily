class Solution {
public:
    int countPermutations(vector<int>& complexity) {
        
        int n = complexity.size();
        long long int ans = 1;
        const int mod = 1e9 + 7;

        for (int i = 1; i < n; i++) {
            if(complexity[i] <= complexity[0]) {
                return 0;
            }
            ans = (ans*1LL*(i))%mod;
        }
        return ans;
    }
};

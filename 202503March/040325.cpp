// https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/?envType=daily-question&envId=2025-03-04

class Solution {
    public:
        bool checkPowersOfThree(int n) {
            if (n<=0) return 0;
            while(n>0){
                auto[q, r] = div(n, 3);
                if (r == 2) return 0;
                n = q;
            }
            return 1;
        }
    };
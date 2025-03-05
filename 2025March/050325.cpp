// https://leetcode.com/problems/count-total-number-of-colored-cells/submissions/1563517331/?envType=daily-question&envId=2025-03-05

class Solution {
    public:
        long long coloredCells(int n) {
            return 2LL*n*(n-1)+1;
        }
    };
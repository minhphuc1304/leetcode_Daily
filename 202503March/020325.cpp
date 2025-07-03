// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/?envType=daily-question&envId=Invalid%20Date

class Solution {
    public:
        vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
            int n=nums1.size(), m=nums2.size();
    
            vector<vector<int>> ans;
    
            int n1=0, n2=0;
            while(n1<n && n2<m){
                if(nums1[n1][0]==nums2[n2][0]){
                    ans.push_back({nums1[n1][0],nums1[n1][1]+nums2[n2][1]});
                    n1++,n2++;
                }
                else if(nums1[n1][0]<nums2[n2][0]){
                    ans.push_back({nums1[n1][0],nums1[n1][1]});
                    n1++;
                }else{
                    ans.push_back({nums2[n2][0],nums2[n2][1]});
                    n2++;
                }
            }
            while(n1<n){
                ans.push_back({nums1[n1][0],nums1[n1][1]});
                n1++;
            }
            while(n2<m){
                ans.push_back({nums2[n2][0],nums2[n2][1]});
                n2++;
            }
            return ans;
        }
    };
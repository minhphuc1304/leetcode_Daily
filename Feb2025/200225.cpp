// https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2025-02-20
class Solution {
    public:
        string res = "";
        void solve(int n, unordered_map<string,int>&mp, int idx,string curr){
            if(idx >= n){
                if(mp.find(curr) == mp.end()){
                    res = curr;
                }
                return;
            }
            solve(n,mp,idx+1,curr+'0');
            // curr.pop_back();
            solve(n,mp,idx+1,curr+'1');
            // curr.pop_back();
        }
        string findDifferentBinaryString(vector<string>& nums) {
            int n = nums.size();
            unordered_map<string,int>mp;
            for(auto str : nums){
                mp[str]++;
            }
            solve(n,mp,0,"");
            return res;
        }
    };
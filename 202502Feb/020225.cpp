class Solution {
public:
    bool check(vector<int>& nums) {
        //sequence should be first decreasing
        //then increasing in case of rotations > 0
        int n=nums.size();
        vector<int>break_points;
        for(int i=1;i<n;i++){
            if(nums[i]<nums[i-1]){
                break_points.push_back(i);
            }
        }
        if(break_points.size()>1){
            //array is not sorted
            return false;
        }
        if(break_points.size()==0){
            //array is increasing and with 0 rotation
            return true;
        }
        //cout<<break_points[0]<<" ";
        int max_elem_before_break=0,min_elem_before_break=INT_MAX;
        for(int i=0;i<break_points[0];i++){
            max_elem_before_break=max(max_elem_before_break,nums[i]);
            min_elem_before_break=min(min_elem_before_break,nums[i]);
        }
        //cout<<min_elem_before_break<<", "<<max_elem_before_break;
        for(int i=break_points[0];i<n;i++){
            if(nums[i]>max_elem_before_break){
                return false;
            }
            if(nums[i]>min_elem_before_break){
                return false;
            }
        }
        return true;
    }
};
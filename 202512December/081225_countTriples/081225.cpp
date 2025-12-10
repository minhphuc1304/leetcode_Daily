class Solution {
public:
    int countTriples(int n) {
        int count = 0;
       
        int arr[n+1]; 
        
        for(int i = 1; i <= n; i++) {
            arr[i] = i * i; // Store the square
            
            // Step 3: Two Pointers approach
            // Find two numbers (left and right) whose squares sum to arr[i]
            int left = 1;
            int right = i - 1;
            
            while(left <= right) {
                int currentSum = arr[left] + arr[right];
                int target = arr[i];
                
                if(currentSum == target){
                    // Found a triple! (e.g., 3^2 + 4^2 = 5^2)
                    count += 2;
                    left++;
                    right--;
                }
                else if(currentSum < target) left++;
                else right--;
            }
        }
        return count;
    }
};
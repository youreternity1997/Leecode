// https://leetcode.com/problems/product-of-array-except-self/solutions/4876857/simple-easy-approach-prefixsum-beats-73-94-c-java-kotlin/
// Time complexity: O(n)
// Space complexity: O(1)

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>left(n,1);
        vector<int>right(n,1);
        left[0] = 1;
        for(int i=1; i<n; i++){
            left[i] = left[i-1]*nums[i-1];
        }

        right[n-1] = 1;
        for(int i=n-2; i>=0; i--){
           right[i] = right[i+1]*nums[i+1];
        }
       vector<int>result(n);
       for(int i=0; i<n; i++){
           result[i] = left[i]*right[i];
       }
       
        return result;
    }
};
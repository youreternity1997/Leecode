// https://www.youtube.com/watch?v=b4oyNbYLSk4
// Time O(n)
// Space O(1)

class Solution {
public:
    int longestSubsequence(string s, int k) {
        int n = s.size(), res = 0, sum = 0;

        for(int i=n-1; i>=0; i--){
            int num = s[i]-'0';
            if(num == 0)
                res++;
            else{
                int j = n-i-1;
                if(sum + pow(2, j) <= k){
                    sum += pow(2, j);
                    res++;
                }
            }
        }
        return res;
    }
};
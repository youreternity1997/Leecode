// https://ithelp.ithome.com.tw/articles/10326088

class Solution {
public:
    string removeDuplicates(string s) {
        string ans ;
        for (int i=0;i<s.size();i++) {
            if(ans.empty()){
                ans +=s[i];
            }
            else if(ans.back() == s[i])
                ans.pop_back();
            else
                ans +=s[i];
        }
        return ans;
    }
};
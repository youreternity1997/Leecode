// https://ithelp.ithome.com.tw/articles/10326088

class Solution {
public:
    int calPoints(vector<string>& operations) {
        int ans = 0;
        int tmp1,tmp2;
        stack<int>score;
        for(string ch :operations){
            if(ch == "+"){
                tmp1 = score.top();
                score.pop();
                tmp2 = score.top();
                score.push(tmp1);
                score.push(tmp1+tmp2);

            }
            else if(ch =="D"){
                tmp1 = score.top();
                score.push(tmp1*2);
            }
            else if(ch == "C"){
                score.pop();
            }
            else{
                score.push(stoi(ch));
            }
        }
        while(score.size()>0){
            ans+=score.top();
            score.pop();
        }
        return ans;
    }
};
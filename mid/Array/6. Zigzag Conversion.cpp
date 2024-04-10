class Solution {
public:
    string convert(string inputString, int numRows) {
        if (numRows <= 1) return inputString;
        
        vector<string> rows(min(numRows, int(inputString.size())), "");
        int direction = -1; // -1 represents down, 1 represents up
        int currentRow = 0;
        
        for (int i = 0; i < inputString.size(); i++) {
            rows[currentRow] += inputString[i];
            currentRow += (direction == -1) ? 1 : -1;
            
            if (currentRow == 0 || currentRow == numRows - 1) {
                direction = -direction;
            }
        }
        
        string result = "";
        for (const auto& row : rows) {
            result += row;
        }
        
        return result;
    }
};

int main(){
    string s = "PAYPALISHIRING";
    int numRows = 3;
    string ans = Solution().convert(s, numRows);
    cout << ans;

}
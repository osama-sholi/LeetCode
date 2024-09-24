class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1){
            return s;
        }
        
        vector<string> zig(numRows);
        for(int i=0;i<numRows;i++){
            zig[i] = "";
        }

        int i;
        int row = 0;

        while(i < s.length()){
            while(i < s.length() && row<numRows){
                zig[row] += s[i];
                i++;
                row++;
            }

            row -= 2;
            while(i < s.length() && row > 0){
                zig[row] += s[i];
                i++;
                row--;
            }
        }

        string result = "";
        for(int j=0; j<numRows; j++){
            result += zig[j];
        }

        return result;
    }
};
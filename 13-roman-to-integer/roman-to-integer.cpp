class Solution {
public:
    int romanToInt(string s) {
        map<char,int> roman;
        roman['I'] = 1;
        roman['V'] = 5;
        roman['X'] = 10;
        roman['L'] = 50;
        roman['C'] = 100;
        roman['D'] = 500;
        roman['M'] = 1000;

        int result = 0;
        for(int i = 0;i < s.length(); i++){
            int number = roman[s[i]];
            if(number < roman[s[i + 1]]){
                number = roman[s[i + 1]] - number;
                i++;
            }
            result += number;
        }

        return result;
    }
};
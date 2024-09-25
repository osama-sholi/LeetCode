class Solution {
    int index;
    string getWord(string s){
        string word = "";
        for(int i = index; index < s.length() && !isspace(s[i]) ;i++){
            word += s[i];
            index++;
        }
        index++;
        return word;
    }
public:
    bool wordPattern(string pattern, string s) {
        map<string,char> m;
        map<char,string> m1;
        index = 0;
        for(int i = 0; i < pattern.length(); i++){
            if(index >= s.length()){
                return false;
            }
            
            string word = getWord(s);
            if((m.count(word) && m[word] != pattern[i]) || (m1.count(pattern[i]) && m1[pattern[i]] != word)){
                return false;
            }

            m[word] = pattern[i];
            m1[pattern[i]] = word;
        }

        if(index < (s.length() - 1)){
            return false;
        }

        return true;
    }
};
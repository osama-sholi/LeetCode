class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if(word1.length() != word2.length()){
            return false;
        }

        map<char,int> freq1, freq2;

        int unique1 = 0, unique2 = 0;

        for(int i = 0; i < word1.length(); i++){
            if(freq1.count(word1[i])){
                freq1[word1[i]]++;
            }else{
                freq1[word1[i]] = 1;
                unique1++;
            }

            if(freq2.count(word2[i])){
                freq2[word2[i]]++;
            }else{
                freq2[word2[i]] = 1;
                unique2++;
            }
        }

        if(unique1 != unique2){
            return false;
        }

        vector<int> counts1(unique1);
        vector<int> counts2(unique2);
        for(auto i : freq1){
            if(freq2.count(i.first)){
                counts1.push_back(i.second);
                counts2.push_back(freq2[i.first]);
            }else{
                return false;
            }
        }

        sort(counts1.begin(),counts1.end());
        sort(counts2.begin(),counts2.end());
        
        if(counts1 != counts2){
            return false;
        }

        return true;
    }
};
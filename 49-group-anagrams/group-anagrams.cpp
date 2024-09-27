class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>> m;
        for (int i = 0; i < strs.size(); i++) {
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            m[temp].push_back(strs[i]);
        }

        vector<vector<string>> result;
        for(auto it : m){
            vector<string> v;
            for(int i = 0; i < it.second.size(); i++){
                v.push_back(it.second[i]);
            }
            result.push_back(v);
        }

        return result;
    }
};
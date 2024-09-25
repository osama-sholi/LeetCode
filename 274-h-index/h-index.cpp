class Solution {
    int min(int x, int y){
        if(x < y){
            return x;
        }else{
            return y;
        }
    }
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end(),greater<int>());
        int h = citations[0];
        int count = 1;
        for(int i = 1; i<citations.size();i++){
            if(count > citations[i]){
                break;
            }
            count++;
            h = citations[i];
        }

        return min(count,h);
    }
};
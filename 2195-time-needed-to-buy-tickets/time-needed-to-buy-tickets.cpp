class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int seconds = 0;
        int i = 0;
        while(tickets[k]){
            if(tickets[i] == 0){
                i = (i + 1) % tickets.size();
                continue;
            }
            tickets[i]--;
            seconds++;
            i = (i + 1) % tickets.size();
        }

        return seconds;
    }
};
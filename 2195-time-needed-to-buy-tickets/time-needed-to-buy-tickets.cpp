class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int seconds = 0;
        while (true) {
            tickets[0]--;
            rotate(tickets.begin(), tickets.begin() + 1, tickets.end());

            if (tickets[tickets.size() - 1] == 0) {
                if (k == 0) {
                    seconds++;
                    return seconds;
                }
                tickets.pop_back();
            }
            if (k == 0) {
                k = tickets.size() - 1;
            }
            else {
                k--;
            }
            seconds++;
        }
    }
};
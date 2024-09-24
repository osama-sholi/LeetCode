class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyDay = 0,sellDay = prices.size() - 1,buyCand = 0;
        for(int i=1;i<prices.size();i++){
            if(prices[i] < prices[buyCand]){
                buyCand = i;
                if(i<sellDay){
                    buyDay = buyCand;
                }
            }
            if((prices[i] - prices[buyCand]) > (prices[sellDay] - prices[buyDay])){
                sellDay = i;
                buyDay = buyCand;
            }
        }
        cout << buyDay << sellDay;
        return prices[sellDay] - prices[buyDay];
    }
};
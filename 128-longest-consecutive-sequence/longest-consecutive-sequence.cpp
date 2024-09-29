class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() < 1){
            return 0;
        }
        sort(nums.begin(),nums.end());
        int max = 1;
        int counter = 1;
        for(int i = 1;i < nums.size();i++){
            if(abs(nums[i] - nums[i-1]) == 1) counter++;
            else{
                if(counter > max) max = counter;

                if(nums[i] != nums[i-1]) counter = 1;
            }
        }

        if(counter > max) max = counter;
        

        return max;
    }
};
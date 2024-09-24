class Solution {
    bool passable(vector<int>& nums, int& i){
        int neededSteps = 2;
        for(int j = i-1;j >= 0;j--){
            if(nums[j] >= neededSteps){
                i=j;
                return true;
            }
            neededSteps++;
        }
        return false;
    }

public:
    bool canJump(vector<int>& nums) {
        for(int i = nums.size() - 2; i >= 0; i--){
            if(nums[i] == 0 && !passable(nums, i)){
                return false;
            }
        }
        return true;
    }
};
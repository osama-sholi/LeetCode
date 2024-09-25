class Solution {
    vector<int> v;
    int steps;

    void recursion(int index){
        if(v[index] >= (v.size() - 1 - index)){
            steps++;
            return;
        }
        int bestNextIndex = v[index] + index;
        int bestStep = bestNextIndex + v[bestNextIndex];

        for(int i = v[index] -1; i > 0 ; i--){
            int nextIndex = index + i;
            int stepStrength = nextIndex + v[nextIndex];
            if(v[nextIndex] > 0){
                if(stepStrength > bestStep){
                    bestStep = stepStrength;
                    bestNextIndex = nextIndex;
                }
            }
            
        }

        steps++;
        recursion(bestNextIndex);
    }

public:
    int jump(vector<int>& nums) {
        if(nums.size() == 1){
            return 0;
        }
        v = nums;
        steps = 0;
        recursion(0);
        return steps;
    }
};
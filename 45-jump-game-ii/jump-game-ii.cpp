class Solution {
    vector<int> v;
    int steps;

    void recursion(int index){
        cout << index << endl;
        if(v[index] >= (v.size() - 1 - index)){
            steps++;
            return;
        }
        int bestStepSize = v[index];
        int bestStep = bestStepSize + index + v[bestStepSize + index];

        for(int i = v[index] -1; i > 0 ; i--){
            int nextIndex = index + i;
            int stepStrength = nextIndex + v[nextIndex];
            //if(stepStrength > (index + v[index]))
            if(v[nextIndex] > 0){
                if(stepStrength > bestStep){
                    bestStep = stepStrength;
                    bestStepSize = i;
                }
            }
            
        }

        steps++;
        recursion(bestStepSize + index);
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
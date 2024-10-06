class Solution {
    // the counter
    int steps;

    void recursion(int index, int prevRear, vector<int>& v){
        // if we can reach the end directly from this index
        if(v[index] >= (v.size() - 1 - index)){
            steps++;
            return;
        }

        // the farthest index we can reach in the next two steps
        int bestIndex = prevRear;

        // we start comparing the choices of the current index
        for(int i = prevRear + 1; i <= (index + v[index]) ; i++){
            if((i + v[i]) > (bestIndex + v[bestIndex])){
                bestIndex = i;
            }
        }

        // we add a step and go to the chosen index
        steps++;
        recursion(bestIndex, index + v[index] + 1, v);
    }

public:
    int jump(vector<int>& nums) {
        if(nums.size() == 1){
            return 0;
        }
        steps = 0;
        recursion(0,1,nums);
        return steps;
    }
};
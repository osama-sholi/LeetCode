class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxValue = 0;
        int i = 0;
        int j = height.size() - 1;
        while(i!=j){
                            cout << i << endl << j << endl;

            int area = min(height[i],height[j]) * (j-i);
            if(area > maxValue){
                maxValue = area;
            }
            if(height[i] > height[j]){
                j--;
            }else{
                i++;
            }
        }
        return maxValue;
    }
};
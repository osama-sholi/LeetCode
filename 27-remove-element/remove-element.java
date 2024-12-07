class Solution {
    public int removeElement(int[] nums, int val) {
        int size = nums.length;
        for(int i = 0, j = nums.length - 1; i <= j; i++){
            if(nums[i] == val){
                for(;j > i && nums[j] == val; j--){
                    size--;
                }
                nums[i] = nums[j];
                j--;
                size--;
            }
        }
        return size;
    }
}
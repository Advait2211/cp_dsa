class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        // bubble sort
        for(int i = 0; i < nums.size(); i++){
            auto swapped = "False";
            for(int j = 0; j < nums.size() - i - 1; j++){
                if (nums[j] > nums[j+1]){
                    swap(nums[j], nums[j+1]);
                    swapped = "True";
                };
            };
            if (swapped == "False"){
                break;
            }
            
        };

        return nums;
    }
};
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        if( nums.size() == 0) return 1;
        for(int i=1;i<= nums.size();i++){
            if(find(nums.begin(),nums.end(),i) != nums.end()){
               ;
            }
            else{
                if( i < nums[nums.size()-1]) return i;
            }
        }
        return nums[nums.size()-1]+1;
    }   
};

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        for i in range(len(nums)):
            c= target - nums[i]
            if( c in nums[i+1:]):
                return [i,nums.index(c)]

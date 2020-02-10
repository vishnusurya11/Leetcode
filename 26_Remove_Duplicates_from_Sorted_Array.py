class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (not len(nums)) or (len(nums) == 1) : return len(nums)
        pointer = 0
        while 1:
            if nums[pointer] == nums[pointer+1]:
                nums.remove(nums[pointer+1])
            else:
                pointer = pointer + 1
            if pointer == len(nums)-1:
                break
        return len(nums)
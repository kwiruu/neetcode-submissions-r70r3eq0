class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i, num in enumerate(nums):
            if i < len(nums) - 1:    
                if nums[i + 1] == num:
                    return True
        return False
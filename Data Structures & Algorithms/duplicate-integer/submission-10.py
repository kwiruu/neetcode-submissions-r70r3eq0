class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i, num in zip(nums, nums[1:]):
            if i == num: return True
        return False
class Solution:
    def bin_search(self, low: int, high: int, nums: List[int], target:int) -> int:
        if low > high:
            return -1
        
        middle = low + (high-low) // 2

        if target == nums[middle]: 
            return middle
        if nums[middle] > target:
            return self.bin_search(low, middle-1, nums, target)
        else:
            return self.bin_search(middle+1, high, nums, target)
        
    def search(self, nums: List[int], target: int) -> int:
        
        return self.bin_search(0, (len(nums)-1), nums, target)
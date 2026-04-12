class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            middlez = low + ((high-low) // 2)
            value = nums[middlez]

            if target == nums[middlez]: return middlez
            if value > target: high = middlez-1
            elif value < target: low = middlez+1
            else: return middlez

        return -1
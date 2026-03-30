class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i, num in enumerate(nums):
            total = 1
            for j, n in enumerate(nums):
                if j == i:
                    continue
                print(nums[j])
                total *= nums[j]
            output.append(total)
        return output
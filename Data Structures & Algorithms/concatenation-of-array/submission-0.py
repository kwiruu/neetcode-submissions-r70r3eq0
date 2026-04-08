class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []

        for i in range(len(nums)):
            nums.append(nums[i])
        return nums

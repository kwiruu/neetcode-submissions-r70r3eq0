class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        temp = 0
        maxz = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = 0
                
            if nums[i] == 1:
                temp += 1
            
            maxz = max(temp, maxz)
        
        return maxz
            

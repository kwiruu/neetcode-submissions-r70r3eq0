class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = sorted(list(set(nums)))
        print(temp)
        if len(nums) == 0:
            return 0
        maxz = 1
        streak = 1
        for j, numz in enumerate(range(len(temp)-1)):
            if temp[j]+1 == temp[j+1]:
                streak += 1
            else:
                maxz = max(streak, maxz)
                streak = 1
        return max(maxz, streak)
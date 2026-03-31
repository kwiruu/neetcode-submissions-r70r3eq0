class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        longest = 0
        for num in temp:
            length = 0
            #check if num has left neighbor
            if num-1 not in temp:
                while (num + length) in temp:
                    length += 1
            longest = max(length, longest)
        return longest

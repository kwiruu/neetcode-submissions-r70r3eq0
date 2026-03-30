class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for num in nums:
            if num not in temp:
                temp[num] = 0
            temp[num] += 1
        
        numz = sorted(temp, key=lambda x: temp[x], reverse=False)
        return numz[-k:]

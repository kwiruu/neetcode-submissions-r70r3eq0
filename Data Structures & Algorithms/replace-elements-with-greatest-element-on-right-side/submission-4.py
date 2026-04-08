class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        for i in range(len(arr)-1, -1, -1):
            newMaxi = max(arr[i], maxi)
            arr[i] = maxi
            maxi = newMaxi
        return arr
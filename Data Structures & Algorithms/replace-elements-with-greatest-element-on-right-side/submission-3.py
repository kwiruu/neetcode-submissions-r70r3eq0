class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-1
        maxi = -1
        while i >= 0:
            newMaxi = max(arr[i], maxi)
            arr[i] = maxi
            maxi = newMaxi
            i -= 1
        return arr
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        y = list(t)
        x.sort()
        y.sort()
        if len(x) != len(y):
            return False
        for i, letter in enumerate(x):
            if x[i] == y[i]:
                pass
            else:
                return False
        return True
        
        
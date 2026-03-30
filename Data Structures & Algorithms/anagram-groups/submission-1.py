class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temps = {}
        for i, s in enumerate(strs):
            
            key = "".join(sorted(s))

            if key not in temps:
                temps[key] = []

            temps[key].append(s)
            strings = list(temps.values())
        return strings
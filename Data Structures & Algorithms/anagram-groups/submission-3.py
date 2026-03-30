class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temps = {}
        for s in strs:
            key = "".join(sorted(s))

            if key not in temps:
                temps[key] = []
            
            temps[key].append(s)
            
        string = list(temps.values())
        return string
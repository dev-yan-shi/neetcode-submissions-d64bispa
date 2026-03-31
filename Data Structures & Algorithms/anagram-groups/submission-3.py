class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for i in range(len(strs)):
            sorted_string = "".join(sorted(strs[i]))
            if sorted_string in out.keys():
                out[sorted_string].append(strs[i])
            else:
                out[sorted_string] = [strs[i]]
        return list(out.values())
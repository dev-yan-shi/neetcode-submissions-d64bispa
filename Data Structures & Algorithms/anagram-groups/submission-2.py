class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #freq_arr = [[0]*26 for i in range(len(strs))]
        out = {}
        #print(freq_arr)
        for i in range(len(strs)):
            freq_arr = [0] * 26
            for char in strs[i]:
                #freq_arr[i][ord(char) - ord('a')] +=1
                freq_arr[ord(char) - ord('a')] +=1
                #print(freq_arr[i])
            if tuple(freq_arr) in out.keys():
                out[tuple(freq_arr)].append(strs[i])
            else:
                out[tuple(freq_arr)] = [strs[i]]
        
        #freq_arr = [tuple(freq_arr[i]) for i in range(len(strs))]
        #print(freq_arr)
        
        # out = {}
        # for i in range(len(strs)):
        #     if freq_arr[i] in out.keys():
        #         out[freq_arr[i]].append(strs[i])
        #     else:
        #         out[freq_arr[i]] = [strs[i]]
        #print(out)
        return list(out.values())

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for n in nums:
            if n in freq_dict.keys():
                freq_dict[n] +=1
            else:
                freq_dict[n] = 1
        #out = [key for key,value in freq_dict.items() if value>=k]
        freq_dict = {k:v for k,v in sorted(freq_dict.items(), key = lambda x: x[1], reverse=True)}
        #print(freq_dict)
        return list(freq_dict.keys())[:k]
        
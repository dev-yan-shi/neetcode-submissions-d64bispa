class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_list = [[] for i in range(len(nums) + 1)]
        for n in nums:
            freq_map[n] = 1+ freq_map.get(n, 0)
        
        for n,f in freq_map.items():
            freq_list[f].append(n)
        
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res)==k:
                    return res
        
        
            
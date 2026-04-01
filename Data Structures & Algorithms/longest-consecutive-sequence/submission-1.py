class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        freq = {}
        for i in range(len(nums)):
            curr = heapq.heappop(nums)
            if curr-1 in freq.keys():
                freq[curr] = freq[curr-1] + 1
            else:
                freq[curr] = 1
        return max(freq.values())
            
        
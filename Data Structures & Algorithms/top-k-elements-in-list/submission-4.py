class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        counts = {}
        for n in nums:
            c = counts.get(n)
            if c == None:
                counts[n] = 0
            else:
                counts[n] = counts[n] + 1
        sorted_numbers = sorted(counts, key=counts.get, reverse=True)
        return sorted_numbers[0:k]
            

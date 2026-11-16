class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        asc = {k: v for k, v in sorted(seen.items(), key=lambda item: item[1])}
        result = []
        while k != 0:
            result.append(list(asc)[-(k)])
            k -= 1
        return result 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortedNums = sorted(nums)
        print(sortedNums)
        for i in range(len(sortedNums)):
            if sortedNums[i] > 0:
                break
            if i > 0 and sortedNums[i] == sortedNums[i -1]:
                continue
            l = i + 1
            r = len(sortedNums) - 1
            while l < r:
                total = sortedNums[i] + sortedNums[l]+ sortedNums[r]
                if total == 0:
                    res.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1
                    while sortedNums[l] == sortedNums[l - 1] and l < r:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res
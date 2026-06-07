class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestLen = 0
        setNum = set(nums)
        for num in setNum:
            if num -1 not in setNum:
                step = 0
                while num + step in setNum:
                    step += 1
                longestLen = max(longestLen, step)
        return longestLen
        
                
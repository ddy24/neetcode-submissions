class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum =set(nums)
        longest = 0
        
        for i in setnum:
            if (i-1) not in setnum:
                length =1
                while (i+length) in setnum:
                    length +=1
                longest = max (length, longest)
        return longest
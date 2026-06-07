class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res #异或运算，自己异或为0，0异或为自己，交换律
        return res
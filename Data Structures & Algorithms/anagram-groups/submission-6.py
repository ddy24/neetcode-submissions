#from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =defaultdict(list)
        for s in strs:
            count = [0]* 26
            for c in s:
                count[ord(c)-ord("a")] +=1 #计算字符c和a之间的偏移量
            res[tuple(count)].append(s)
        return res.values()

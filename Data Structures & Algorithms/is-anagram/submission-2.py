from collections import Counter
class Solution:
    def isAnagram(self, s:str, t: str)->bool:
        dictS = Counter(s)
        dictT = Counter(t)
        if dictS == dictT:
            return True
        else:
            return False
        
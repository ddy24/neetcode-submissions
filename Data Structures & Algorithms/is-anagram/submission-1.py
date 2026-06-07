class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for n in s:
            s_dict[n] += 1
        for m in t:
            t_dict[m] +=1
        return s_dict == t_dict


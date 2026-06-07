class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))+"#"+ string
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            length = s[start:i] 
            string = str(s[i+1: i+1+int(length)])
            res.append(string)
            i = i+1+int(length)
            
        return res
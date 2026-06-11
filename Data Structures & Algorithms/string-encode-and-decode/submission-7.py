class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            length = int(s[start:i])
            string = s[i+1:i+1+length]
            res.append(string)
            i = i+1+length
        return res

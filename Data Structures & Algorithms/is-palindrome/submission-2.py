class Solution:
    def isPalindrome(self, s: str) -> bool:
        sRight = ""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                sRight += s[i].lower()
            if s[i].isdigit():
                sRight += s[i]
        sWithoutBlank = ""
        for j in range(len(s)):
            if s[j].isalpha():
                sWithoutBlank += s[j].lower()
            if s[j].isdigit():
                sWithoutBlank += s[j]
        return sRight == sWithoutBlank

            
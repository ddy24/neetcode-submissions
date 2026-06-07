class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #creat a new list: for each string in strs, order them
        #go through all new string in the new list, if they are same, add the original
        #string to the dictionary:key-> ordered string, value-> original one
        newString = []
        dictionary = defaultdict(list)
        for string in strs:
            stringNew = "".join(sorted(string))
            newString.append(stringNew)
            if stringNew not in dictionary:
                dictionary[stringNew] = [string]
            else:
                dictionary[stringNew].append(string)
        res = []
        for key, val in dictionary.items():
            res.append(val)
        return res
        


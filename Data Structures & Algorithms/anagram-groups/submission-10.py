from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using map: key-> reorder strings, value-> different original strs
        reorderStringMap = defaultdict(list)
        res = []
        #sort原地修改列表，sorted是创建新的修改
        for strings in strs:
            stringsSort = "".join(sorted(strings))
            reorderStringMap[stringsSort].append(strings)
        return list(reorderStringMap.values())
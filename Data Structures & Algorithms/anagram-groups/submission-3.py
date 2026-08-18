class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = {}
        for s in strs:
            key = "".join(sorted(s))

            value = lists.get(key)
            if value == None:
                lists[key] = [s]
            else:
                value.append(s)
                lists[key] = value

        return list(lists.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        value_to_index = {}
        answer_array = []
        index = -1
        for s in strs:
            value = "".join(sorted(s))
            store = value_to_index.get(value)
            if store == None:
                index +=1
                answer_array.append([s])
                value_to_index[value] = index
            else:
                answer_array[store].append(s)
                
        return answer_array
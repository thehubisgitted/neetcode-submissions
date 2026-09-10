class Solution:

    def encode(self, strs: List[str]) -> str:
        empty = ""
        for s in strs:
            substring = str(len(s))+"#"+s
            empty +=substring

        return empty

    def decode(self, s: str) -> List[str]:
        i = 0
        answer = []
        while i < len(s):
            j = i

            while j < len(s):
                if s[j] == "#":
                    break
                j+=1

            length = int(s[i:j])
            start = j + 1
            end = j + length + 1
            word = s[start:end]
            answer.append(word)
            i = end
        
        return answer

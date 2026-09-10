class Solution:

    def encode(self, strs: List[str]) -> str:
        empty = ""
        for s in strs:
            substring = str(len(s))+"#"+s
            empty +=substring
        print("encoded string: "+ empty )
        return empty

    def decode(self, s: str) -> List[str]:
        i = 0
        answer = []
        while i < len(s):
            j = i
            print("j is "+str(j))
            while j < len(s):
                if s[j] == "#":
                    break
                j+=1
            print("end j is "+str(j))
            print("percieved length" + s[i:j])
            length = int(s[i:j])
            start = j + 1
            end = j + length + 1
            word = s[start:end]
            print("decoded substring: "+word)
            answer.append(word)
            i = end
        
        return answer

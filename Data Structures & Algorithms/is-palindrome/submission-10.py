import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
\
        s = "".join(s.lower().split())
        s = re.sub(r'[\W_]', '', s)
        
        start_p = 0
        end_p = len(s) - 1

        while start_p < end_p:
            if s[start_p] != s[end_p]:
                return False
            start_p +=1
            end_p -=1
        return True
        
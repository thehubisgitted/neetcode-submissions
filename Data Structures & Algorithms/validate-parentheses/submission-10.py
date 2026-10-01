class Solution:
    def isValid(self, s: str) -> bool:
        close = {"]":"[", ")":"(", "}":"{"}
        stack = []
        for i in range(len(s)):
            bracket = s[i]
            #close bracket but theres no matching value
            if bracket in close and len(stack) == 0:
                return False
            #open bracket
            elif bracket not in close:
                stack.append(bracket)
            #is a close bracket and the len(stack) > 0
            #check value    
            else:
                value = stack.pop()
                if value != close[bracket]:
                    return False
        #check if theres any orphaned open brackets left
        if len(stack) > 0:
            return False
        else:
            return True
            

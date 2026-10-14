class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
         operands = set(["+","*","-","/"])
         stack = []
         for i in range(0,len(tokens)):
            t = tokens[i]
            
            if t not in operands:
                stack.append(int(t))
            else:
                operand = t
                value = stack.pop()
                previous_value = stack.pop()
                computation = self.mathHelper(operand, previous_value, value)          
                stack.append(computation)
        
         return stack.pop()
    
    def mathHelper(self, operand, one, two):
        if operand == "+":
            return one + two
        elif operand == "-":
            return one - two
        elif operand == "*":
            return one * two
        else:
            return int(one / two)

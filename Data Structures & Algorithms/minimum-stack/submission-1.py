class MinStack:

    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, val: int) -> None:
        if len(self.m) > 0:
            minimum = min(self.m[len(self.m)-1], val)
            self.m.append(minimum)
        else:
            self.m.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.m.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
    def getMin(self) -> int:
        return self.m[len(self.m)-1]

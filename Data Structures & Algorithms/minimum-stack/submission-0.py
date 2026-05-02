class MinStack:

    def __init__(self):
        self.stx = []
        self.min_stx = []

    def push(self, val: int) -> None:
        self.stx.append(val)

        if self.min_stx:
            val = min(val, self.min_stx[-1])
            self.min_stx.append(val)
        else:
            self.min_stx.append(val)

    def pop(self) -> None:
        self.stx.pop()
        self.min_stx.pop()
    def top(self) -> int:
        return self.stx[-1]
    def getMin(self) -> int:
        return self.min_stx[-1]

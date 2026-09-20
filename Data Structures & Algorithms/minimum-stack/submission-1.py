class MinStack:

    def __init__(self):
        self.dq = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.dq.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        self.minstack.append(val)

    def pop(self) -> None:
        self.dq.pop()
        self.minstack.pop()


    def top(self) -> int:
        return self.dq[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


        

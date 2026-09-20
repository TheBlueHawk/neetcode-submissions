class MinStack:

    def __init__(self):
        self.dq = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.dq.append(val)
        if len(self.minstack) > 0:
            minimum = self.minstack.pop() 
            self.minstack.append(minimum)
            self.minstack.append(min(minimum, val))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.dq.pop()
        self.minstack.pop()


    def top(self) -> int:
        v = self.dq.pop()
        self.dq.append(v)
        return v

    def getMin(self) -> int:
        minimum = self.minstack.pop()
        self.minstack.append(minimum)
        return minimum


        

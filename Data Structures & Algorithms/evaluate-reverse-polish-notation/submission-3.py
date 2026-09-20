class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()
        for c in tokens:
            match c:
                case "+":
                    b, a = dq.pop(), dq.pop()
                    dq.append(a+b)
                case "-":
                    b, a = dq.pop(), dq.pop()
                    dq.append(a-b)
                case "*":
                    b, a = dq.pop(), dq.pop()
                    dq.append(a*b)
                case "/":
                    b, a = dq.pop(), dq.pop()
                    dq.append(int(a/b))
                case _:
                    dq.append(int(c))
        return dq[0]

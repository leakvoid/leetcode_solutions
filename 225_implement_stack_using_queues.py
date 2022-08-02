from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        t_q = deque()
        for i in range(len(self.q) - 1):
            t_q.append( self.q.popleft() )
        r = self.q.popleft()
        self.q = t_q
        return r

    def top(self) -> int:
        r = self.pop()
        self.q.append(r)
        return r

    def empty(self) -> bool:
        return (len(self.q) == 0)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

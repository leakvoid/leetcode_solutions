class MyQueue:

    def __init__(self):
        self.stack = []
        # stack append, pop
        # queue append, popleft

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        t_stack = []
        for i in range(len(self.stack) - 1):
            t_stack.append( self.stack.pop() )
        r = self.stack.pop()
        
        self.stack = []
        for i in range(len(t_stack)):
            self.stack.append( t_stack.pop() )
        return r

    def peek(self) -> int:
        t_stack = []
        for i in range(len(self.stack) - 1):
            t_stack.append( self.stack.pop() )
        r = self.stack.pop()
        
        self.stack = []
        self.stack.append( r )
        for i in range(len(t_stack)):
            self.stack.append( t_stack.pop() )
        return r

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

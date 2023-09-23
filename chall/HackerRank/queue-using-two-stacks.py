import sys

class Stack:
    def __init__(self):
        self.l = []
    def pop(self):
        try:
            return self.l.pop()
        except IndexError:
            return None
    def push(self, e):
        self.l.append(e)
        return self
    def isEmpty(self):
        return len(self.l) == 0
    def peek(self):
        try:
            return self.l[-1]
        except IndexError:
            return None

class Queue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    def enqueue(self, e):
        self.inStack.push(e)
        return self
    def _drain(self):
        if self.outStack.isEmpty():
            while e := self.inStack.pop():
                self.outStack.push(e)
    def dequeue(self):
        self._drain()
        return self.outStack.pop()
    def peek(self):
        self._drain()
        return self.outStack.peek()


q = Queue()
for action in sys.stdin.readlines():
    action = action.strip().split(' ')
    if action[0] == '1':
        q.enqueue(action[1])
    elif action[0] == '2':
        q.dequeue()
    elif action[0] == '3':
        print(q.peek())
    else:
        continue

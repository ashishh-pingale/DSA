def __init__(self):
    self.stack = []
    self.min_stack = []


def push(self, value):
    self.stack.append(value)

    if not self.min_stack:
        self.min_stack.append(value)
    else:
        current_min = min(value , self.min_stack[-1])
        self.min_stack.append(current_min)

    
def pop(self):
    self.stack.pop()
    self.min_stack.pop()


def top(self):
    return self.stack[-1]


def getMin(self):
    return self.min_stack[-1]
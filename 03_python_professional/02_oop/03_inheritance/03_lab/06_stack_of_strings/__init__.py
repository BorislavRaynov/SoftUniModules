class Stack:
    data = list()

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

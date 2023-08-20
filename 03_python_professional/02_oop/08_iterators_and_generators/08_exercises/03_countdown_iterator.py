class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.end = 0
        self.start = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.end:
            raise StopIteration

        self.start -= 1
        self.count -= 1

        return self.start



# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

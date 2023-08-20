class sequence_repeat:
    def __init__(self, seq: str, num: int):
        self.seq = seq
        self.num = num

        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.num:
            raise StopIteration

        self.index += 1
        return self.seq[self.index % len(self.seq)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

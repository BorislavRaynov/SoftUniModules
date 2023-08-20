class dictionary_iter:
    def __init__(self, data: dict):
        self.data = list(data.items())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration

        return self.data.pop(0)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

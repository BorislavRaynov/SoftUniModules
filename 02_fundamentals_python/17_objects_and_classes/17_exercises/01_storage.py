class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.string = ""

    def add_product(self, string):
        self.string = string
        if len(self.storage) < self.capacity:
            self.storage.append(string)

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())

class Customer:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id = id_number
        self.rented_dvds = list()

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join(d.name for d in self.rented_dvds)})"

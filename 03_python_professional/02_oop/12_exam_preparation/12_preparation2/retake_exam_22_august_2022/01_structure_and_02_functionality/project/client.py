class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.meals_to_be_ordered = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if not (value.startswith("0") and len(value) == 10 and all(v.isdigit() for v in value)):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

    def meals_name_in_cart(self):
        names = []
        for n in self.meals_to_be_ordered.keys():
            names.append(n)
        return f"{', '.join(names)}"

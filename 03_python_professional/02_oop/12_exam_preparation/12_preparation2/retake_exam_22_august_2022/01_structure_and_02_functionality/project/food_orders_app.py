from project.client import Client


class FoodOrdersApp:
    VALID_TYPES = ['Starter', 'MainDish', 'Dessert']
    receipt_id = 0

    def __init__(self):
        self.menu = list()
        self.clients_list = list()

    def register_client(self, client_phone_number: str):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in FoodOrdersApp.VALID_TYPES:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = [meal.details() for meal in self.menu]
        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.clients_list.append(Client(client_phone_number))

        current_meals = [m.name for m in self.menu]

        for m in meal_names_and_quantities.keys():
            if m not in current_meals:
                raise Exception(f"{m} is not on the menu!")

        for meal in self.menu:
            if meal.name in meal_names_and_quantities:
                if meal.quantity < meal_names_and_quantities[meal.name]:
                    raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        for m, q in meal_names_and_quantities.items():
            if m not in client.meals_to_be_ordered:
                client.meals_to_be_ordered[m] = 0
            client.meals_to_be_ordered[m] += q

        for meal in self.menu:
            if meal.name in meal_names_and_quantities:
                client.shopping_cart.append(meal)
                meal.quantity -= meal_names_and_quantities[meal.name]
                client.bill += meal_names_and_quantities[meal.name] * meal.price

        return f"Client {client_phone_number} successfully ordered {client.meals_name_in_cart()} for "\
               f"{client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):

        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in self.menu:
            if meal.name in client.meals_to_be_ordered:
                meal.quantity += client.meals_to_be_ordered[meal.name]

        client.shopping_cart = []
        client.bill = 0
        client.meals_to_be_ordered = {}

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        total_paid_money = f"{client.bill:.2f}"
        client.shopping_cart = []
        client.bill = 0
        client.meals_to_be_ordered = {}

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money} was successfully paid for "\
               f"{client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

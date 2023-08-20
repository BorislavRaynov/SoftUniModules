from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    def __init__(self, comfort: int = 5, price: float = 10):
        super().__init__(comfort, price)

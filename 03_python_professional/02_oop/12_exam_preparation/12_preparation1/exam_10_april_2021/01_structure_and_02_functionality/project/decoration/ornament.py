from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    def __init__(self, comfort: int = 1, price: float = 5):
        super().__init__(comfort, price)

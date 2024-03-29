from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        pass

    @abstractmethod
    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        pass

    def add_decoration(self, decoration):
        pass

    def feed(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

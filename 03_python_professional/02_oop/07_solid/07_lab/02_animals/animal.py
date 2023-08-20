from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "Cat sound"


class Dog(Animal):

    def make_sound(self):
        return "Dog sound"


animals = [Cat(), Dog()]


def animals_sounds(lst_animals):
    for animal in lst_animals:
        print(animal.make_sound())

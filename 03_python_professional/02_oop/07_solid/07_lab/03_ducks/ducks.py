from abc import abstractmethod, ABC


class Duck(ABC):

    @staticmethod
    @abstractmethod
    def quack():
        pass


class Walkable:

    @staticmethod
    def walk():
        pass


class Flyable:

    @staticmethod
    def fly():
        pass


class RubberDuck(Duck, Walkable):
    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def walk():
        return "rubber walking"


class RobotDuck(Duck, Walkable, Flyable):
    HEIGHT = 50

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return "robot duck walking"

    @staticmethod
    def fly():
        pass

    @staticmethod
    def land():
        RobotDuck.HEIGHT = 0

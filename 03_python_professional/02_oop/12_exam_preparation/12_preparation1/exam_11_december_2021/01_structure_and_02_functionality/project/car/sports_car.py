from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED = 400
    MAX_SPEED = 600

    def __init__(self, model, speed_limit):
        super(SportsCar, self).__init__(model, speed_limit)


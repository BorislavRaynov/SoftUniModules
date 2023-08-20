class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        radius = self.diameter / 2
        return 2 * Circle.__pi * radius

    def calculate_area(self):
        radius = self.diameter / 2
        return Circle.__pi * radius * radius

    def calculate_area_of_sector(self, angle):
        radius = self.diameter / 2
        return (angle / 360) * Circle.__pi * radius * radius


diameter_of_circle = int(input())
diam = Circle(diameter_of_circle)
angle = int(input())

print(f"{diam.calculate_circumference():.2f}")
print(f"{diam.calculate_area():.2f}")
print(f"{diam.calculate_area_of_sector(angle):.2f}")
